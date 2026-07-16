from src.fetch import get_stock_data, get_stock
from src.plotting import plot_close_price, plot_dividends, plot_stock_splits
from src.info import display_stock_info


def main():
    symbol = input("Enter stock ticker: ").upper()

    df = get_stock_data(symbol)
    stock = get_stock(symbol)

    print(df.head())
    plot_close_price(df, symbol)
    
    display_stock_info(stock)
    plot_dividends(stock,symbol)
    plot_stock_splits(stock,symbol)

if __name__ == "__main__":
    main()