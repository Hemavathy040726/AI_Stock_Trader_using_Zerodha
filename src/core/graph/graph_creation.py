# -------------------------------
# GRAPH CREATION
# -------------------------------
from langgraph.constants import END
from langgraph.graph import StateGraph

from src.core.entity.finance_state import State
from src.core.helpers.desicions import should_continue
from src.core.nodes.financial_instrument_picker_purchase import llm_investment_executor_node,  \
     fetch_stock_tool_node, buy_stock_tool_node
from src.core.nodes.human_approval import human_verification_node
from src.core.nodes.portfolio_allocator import llm_portfolio_node, portfolio_tools_node
from src.core.nodes.transaction_analyzer import llm_transaction_analyzer_node, transaction_analyzer_tools_node


def create_agent():
    graph = StateGraph(State)

    # Add nodes (existing pipeline + investment nodes)
    graph.add_node("llm_analyzer", llm_transaction_analyzer_node)
    graph.add_node("transaction_analyzer_tools", transaction_analyzer_tools_node)
    graph.add_node("portfolio_llm", llm_portfolio_node)
    graph.add_node("portfolio_tools", portfolio_tools_node)
    graph.add_node("llm_investment_executor", llm_investment_executor_node)
    graph.add_node("stock_suggestion_tools", fetch_stock_tool_node)
    graph.add_node("human_verification_node", human_verification_node)
    graph.add_node("stock_buy_tools", buy_stock_tool_node)
    #graph.add_edge("wait_for_user", "llm_investment_executor")

    # Flow
    graph.set_entry_point("llm_analyzer")
    graph.add_conditional_edges("llm_analyzer", should_continue,
                                {"transaction_analyzer_tools": "transaction_analyzer_tools", END: "portfolio_llm"})
    graph.add_edge("transaction_analyzer_tools", "llm_analyzer")
    graph.add_edge("portfolio_llm", "portfolio_tools")
    graph.add_edge("portfolio_tools", "llm_investment_executor")
    graph.add_edge("llm_investment_executor", "stock_suggestion_tools")
    graph.add_edge("stock_suggestion_tools", "human_verification_node")
    graph.add_edge("human_verification_node", "stock_buy_tools")
    graph.add_edge("stock_buy_tools", END)

    return graph.compile()
