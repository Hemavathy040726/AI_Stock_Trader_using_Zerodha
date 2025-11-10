from src.core.entity.finance_state import State
from src.core.tools.stock_buy import buy_stock_tool
from src.core.tools.stock_suggest import  fetch_best_stock_tool
from src.config import llm_client
from langchain_core.messages import SystemMessage, HumanMessage



def llm_investment_executor_node(state: State):
    """
       LLM node that:
       1. Picks best stock using fetch_best_stock_tool
       2. Asks human confirmation
       3. If confirmed, calls buy_stock_tool
       """

    print("\n")
    print("------------------------------------")
    print("Agent 3 : Stock Picker Agent Started")
    print("------------------------------------")


    tools = [fetch_best_stock_tool, buy_stock_tool]
    llm_with_tools = llm_client.bind_tools(tools)

    # Get portfolio equity allocation
    portfolio = state.get("portfolio", {})
    equity_str = portfolio.get("Equity (Stocks)", "₹0.00")
    equity_amount = float(equity_str.replace("₹", "").replace(",", ""))

    # Messages for LLM
    messages = state["messages"] + [
        SystemMessage(content="You are a Stock Picker agent. "
                              "Use fetch_best_stock_tool to pick the best stock for my equity allocation. "
                              "Then ask the human if they want to buy it. "
                              "After confirmation, call 'buy_stock_tool' to place the order."),
        HumanMessage(content=f"My equity allocation is ₹{equity_amount}. Please pick the best stock.")
    ]

    response = llm_with_tools.invoke(messages)
    state["messages"].append(response)
    return state


# -------------------------------
# TOOL NODES: Stock suggestion tool node & stock buy tool node
# -------------------------------
def fetch_stock_tool_node(state: State):
    """Fetch best stock(s) and store in state for human approval."""
    portfolio_equity_amount = state.get("portfolio", {}).get("Equity (Stocks)")
    if portfolio_equity_amount:
        # remove currency formatting if any
        portfolio_equity_amount = float(str(portfolio_equity_amount).replace("₹", "").replace(",", ""))
    result = fetch_best_stock_tool.invoke({"portfolio_equity_amount": portfolio_equity_amount})

    # Store fetched stock in state
    state["investment_instruments"] = [result] if result else []
    state["awaiting_approval"] = True

    print(f"✅ Best stock fetched and stored in state: {state['investment_instruments']}")
    return state



def buy_stock_tool_node(state: State):
    """Execute buy order if human approved."""
    print(f"DEBUG in buy_stock_node: approved={state["approved"]}, instruments={state.get('investment_instruments')}")


    if state["approved"]:
        stock = state["investment_instruments"][0]
        amount = stock.get("investment_amount")
        price = stock.get("price")
        quantity = int(amount / price)  # simple calculation
        symbol = stock.get("tradingsymbol")
        exchange = stock.get("exchange", "NSE")

        confirmation = buy_stock_tool.invoke({
            "symbol": symbol,
            "quantity": quantity,
            "exchange": exchange
        })

        state["executed_order"] = {"confirmation": confirmation}
        state["investment_execution"] = "completed"
        print(f"✅ Stock purchase executed: {confirmation}")
    else:
        state["investment_execution"] = "not_approved"
        print("ℹ️ Purchase not approved by human.")

    return state

