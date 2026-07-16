import yfinance as yf
import pandas as pd

def get_stock_data(symbol: str, period: str = "1mo" ) -> pd.DataFrame:
    """
    Download stock data from Yahoo finance
    """
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df