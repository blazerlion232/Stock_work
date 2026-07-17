import matplotlib.pyplot as plt
from src.stockData import StockData
from src.plotting import(
    plot_close_price,
    plot_dividends,
    plot_stock_splits
)
from src.info import display_stock_info

def main():
    symbol = input("Enter stock ticker: ").upper()
    stock = StockData(symbol)
    history = stock.history()
    display_stock_info(stock.info())
    plot_close_price(history, symbol)
    plot_dividends(stock.dividends(), symbol)
    plot_stock_splits(stock.splits(), symbol)
    plt.show()

if __name__ == "__main__":
    main()
