# -------------------------------
# TOOL REGISTRY
# -------------------------------
from src.core.tools.pdf_reader import pdf_reader_tool
from src.core.tools.portfolio_builder import portfolio_builder_tool
from src.core.tools.stock_buy import buy_stock_tool
from src.core.tools.stock_suggest import fetch_best_stock_tool


def get_all_tools():
    return [pdf_reader_tool, portfolio_builder_tool, fetch_best_stock_tool, buy_stock_tool]

def create_tool_registry():
    tools = get_all_tools()
    return {tool.name: tool for tool in tools}