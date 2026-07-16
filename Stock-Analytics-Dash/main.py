from src.fetch import get_stock_data
from src.plotting import plot_close_price

def main():
    symbol = input("Enter stock ticker: ").upper()
    df = get_stock_data(symbol)
    print(df.head())
    plot_close_price(df, symbol)

if __name__ == "__main__":
    main()