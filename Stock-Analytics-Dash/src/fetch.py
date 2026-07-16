import yfinance as yf
import pandas as pd

def get_stock_data(symbol: str, period: "1mo"):
    """
    Download stock data from Yahoo finance
    """
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df