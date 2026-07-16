import matplotlib.pyplot as plt

def plot_close_price(df, symbol):
    plt.figure(figsize=(12,6))
    plt.plot(df.index,df["Close"])
    plt.title(f"{symbol} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid()
    plt.show()