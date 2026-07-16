import matplotlib.pyplot as plt

def plot_close_price(df, symbol):
    plt.figure(figsize = (12,6))
    plt.plot(df.index,df["Close"])
    plt.title(f"{symbol} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid()
    plt.show()

def plot_dividends(stock, symbol):
    dividend = stock.dividends
    if dividend.empty:
        print("No dividend information available.")
        return
    
    plt.figure(figsize = (10,5))
    plt.bar(dividend.index, dividend.values)
    plt.title(f"{symbol} Dividend History")
    plt.xlabel("Date")
    plt.ylabel("Dividend ($)")
    plt.grid(True)
    plt.show()

def plot_stock_splits(stock, symbol):
    splits = stock.splits
    if splits.empty:
        print("No stock splits history available")
        return
    
    plt.figure(figsize = (10,5))
    plt.stem(splits.index, splits.values)
    plt.title(f"{symbol} Stock Splits")
    plt.xlabel("Dates")
    plt.ylabel("Split Ratio")
    plt.grid(True)
    plt.show()