from kiteconnect import KiteConnect
from langchain_core.tools import tool
from src.config import ZERODHA_API_KEY, ZERODHA_ACCESS_TOKEN

kite = KiteConnect(api_key=ZERODHA_API_KEY)
kite.set_access_token(ZERODHA_ACCESS_TOKEN)

@tool("buy_stock_tool")
def buy_stock_tool(symbol: str, quantity: int, exchange: str = "NSE", market_open: bool = True) -> str:
    """
    Places or queues a market buy order. Queues if market closed.
    """
    try:
        instruments = kite.instruments(exchange)
        instr = next((x for x in instruments if x["tradingsymbol"] == symbol), None)
        if not instr:
            return f"❌ Symbol {symbol} not found on {exchange}."

        if not market_open:
            return f"🕒 Market closed — queued {quantity} shares of {symbol} for next open session."

        order = kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=exchange,
            tradingsymbol=symbol,
            transaction_type=kite.TRANSACTION_TYPE_BUY,
            quantity=quantity,
            order_type=kite.ORDER_TYPE_MARKET,
            product=kite.PRODUCT_CNC
        )

        return f"✅ Live order placed: {quantity} shares of {symbol}, Order ID: {order['order_id']}"

    except Exception as e:
        return f"❌ Failed to place order: {str(e)}"
