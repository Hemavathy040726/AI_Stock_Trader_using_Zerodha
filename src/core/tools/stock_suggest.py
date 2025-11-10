# -------------------------------
# TOOL: Stock Suggestion (live Zerodha)
# -------------------------------
from typing import Annotated

from kiteconnect import KiteConnect
import random

from langchain_core.tools import tool

from src.config import ZERODHA_API_KEY, ZERODHA_ACCESS_TOKEN

import pandas as pd
from kiteconnect import KiteConnect
import os

from datetime import datetime, time

# -------------------------------
# Zerodha API setup
# -------------------------------




# -------------------------------
# Fetch Best Stock Tool
# -------------------------------
@tool("fetch_best_stock_tool")
def fetch_best_stock_tool(portfolio_equity_amount: Annotated[float, "Available money for stock purchase"]) -> dict:
    """
    Selects the best stock to buy using filtered universe + scoring system.
    Returns stock symbol, price, suggested quantity.
    """
    print("Fetching best stock tool")
    # -------------------------------
    # 1️⃣ Fetch all instruments and filter
    # -------------------------------
    print("Fetching best stock tool")

    kite = KiteConnect(api_key=ZERODHA_API_KEY)
    kite.set_access_token(ZERODHA_ACCESS_TOKEN)

    # Step 1: Get all instruments (NSE)
    df = pd.DataFrame(kite.instruments("NSE"))
    print(f"Instruments: {len(df)}")

    # Step 2: Filter equities only
    equity_df = df[df["instrument_type"] == "EQ"]
    print(f"✅ Filtered to {len(equity_df)} valid equity stocks.")

    if len(equity_df) == 0:
        return {"error": "No valid equities found."}

    # Step 3: Random sample of equities (avoid rate limit)
    sample_df = equity_df.sample(100, random_state=42)
    symbols = [f"NSE:{sym}" for sym in sample_df["tradingsymbol"].tolist()]

    # Step 4: Fetch prices (live or last close)
    market_open = is_market_open()
    print("📊 Market open:", market_open)

    ltp_data = kite.ltp(symbols)
    price_rows = []

    for sym, info in ltp_data.items():
        tradingsymbol = sym.split(":")[1]
        price = info.get("last_price", 0.0)
        ohlc = info.get("ohlc", {})
        open_price = ohlc.get("open", price)
        close_price = ohlc.get("close", price)
        change = 0
        if open_price > 0:
            change = (price - open_price) / open_price * 100

        price_rows.append({
            "tradingsymbol": tradingsymbol,
            "price": price,
            "close_price": close_price,
            "change_pct": change
        })

    live_df = pd.DataFrame(price_rows)
    print(f"📈 Got prices for {len(live_df)} stocks")

    # Step 5: Use close_price if market closed
    if not market_open:
        live_df["price"] = live_df["close_price"]

    # Step 6: Sort by positive daily movement (momentum)
    live_df = live_df.sort_values("change_pct", ascending=False)

    best_stock = live_df.iloc[0].to_dict()
    best_stock["investment_amount"] = portfolio_equity_amount
    print("✅ Best stock fetched:", best_stock)

    return best_stock

def is_market_open() -> bool:
    """Check if Indian market is open (NSE timings)."""
    now = datetime.now().time()
    market_open = time(9, 15)
    market_close = time(15, 30)
    return market_open <= now <= market_close