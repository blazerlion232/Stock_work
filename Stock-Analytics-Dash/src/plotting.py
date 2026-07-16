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
    plt.bar(dividend.index, dividend.value)
    plt.title(f"{symbol} Dividend History")
    plt.xlabel("Date")
    plt.ylabel("Dividend ($)")
    plt.grid(True)
    plt.show()