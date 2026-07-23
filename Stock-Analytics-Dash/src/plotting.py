import matplotlib.pyplot as plt
import pandas as pd


def plot_close_price(df: pd.DataFrame, symbol: str):
    plt.figure(figsize = (12,6))
    plt.plot(df.index,df["Close"],label="Close price", linewidth=1.5)

    for column in df.columns:
        if column.startswith(("SMA_", "EMA_")):
            plt.plot(df.index, df[column], label=column, linewidth=1.2)

    plt.title(f"{symbol} Closing Price and Price trend Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

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
