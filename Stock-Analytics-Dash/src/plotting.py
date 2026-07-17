import matplotlib.pyplot as plt
import pandas as pd


def plot_close_price(df, symbol):
    plt.figure(figsize = (12,6))
    plt.plot(df.index,df["Close"])
    plt.title(f"{symbol} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid()

def plot_dividends(dividends: pd.Series, symbol: str):
    if dividends.empty:
        print("No dividend information available.")
        return
    
    plt.figure(figsize = (10,5))
    plt.bar(dividends.index, dividends.values)
    plt.title(f"{symbol} Dividend History")
    plt.xlabel("Date")
    plt.ylabel("Dividend ($)")
    plt.grid(True)

def plot_stock_splits(splits: pd.Series, symbol: str):
    if splits.empty:
        print("No stock splits history available")
        return
    
    plt.figure(figsize = (10,5))
    plt.stem(splits.index, splits.values)
    plt.title(f"{symbol} Stock Splits")
    plt.xlabel("Dates")
    plt.ylabel("Split Ratio")
    plt.grid(True)
