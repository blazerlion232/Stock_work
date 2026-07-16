import yfinance as yf
import pandas as pd

def get_stock(symbol: str):
    """ Return a yfinance ticker object"""
    return yf.Ticker(symbol)

def get_stock_data(symbol: str, period: str = "1mo" ) -> pd.DataFrame:
    stock = get_stock(symbol)
    return stock.history(period=period)