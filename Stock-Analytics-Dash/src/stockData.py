import yfinance as yf
import pandas as pd

class StockData:
    """
    Handles retrieving data from Yahoo Finance
    """
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.stock = yf.Ticker(self.symbol)

    def history(self, period: str = "1y"):
        """
        Download historical stock prices.
        """
        return self.stock.history(period=period)
    def info(self) -> dict:
        """
        Download company information.
        """
        return self.stock.info
    def fast_info(self):
        """
        Quickly retrieve frequently used statistics.
        """
        return self.stock.fast_info
    def dividends(self) -> pd.Series:
        """
        Return historical dividends payments.
        """
        return self.stock.dividends
    def splits(self) -> pd.Series:
        """
        Return historical stock splits.
        """
        return self.stock.splits
    def earnings_dates(self):
        """
        Return upcoming and historical earnings dates.
        """
        return self.stock.earnings_dates
    def recommendations(self):
        """
        Return analyst recommendations.
        """
        return self.stock.recommendations
    def news(self):
        """
        Return recent news articles.
        """
        return self.stock.news
    def financials(self):
        """
        Annual balance sheet.
        """
        return self.stock.balance_sheet
    def cashflow(self):
        """
        Annual cashflow statement
        """
        return self.stock.cashflow