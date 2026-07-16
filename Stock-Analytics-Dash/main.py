from src.fetch import get_stock_data
from src.plotting import plot_close_price
from src.plotting import plot_dividends
from src.info import display_stock_info


def main():
    symbol = input("Enter stock ticker: ").upper()
    df = get_stock_data(symbol)
    print(df.head())
    plot_close_price(df, symbol)
    display_stock_info(df)
    plot_dividends(df,symbol)
if __name__ == "__main__":
    main()