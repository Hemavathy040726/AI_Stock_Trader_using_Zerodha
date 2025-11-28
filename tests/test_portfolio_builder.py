from src.core.tools.portfolio_builder import portfolio_builder_tool

def test_portfolio_builder_basic():
    result = portfolio_builder_tool.invoke({
        "total_savings": 50000,
        "user_age": 35,
        "insured": False
    })
    assert "Equity (Stocks)" in result
    assert "Insurance" in result