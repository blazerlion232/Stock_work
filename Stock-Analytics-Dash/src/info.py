import yfinance as yf

def display_stock_info(stock):
    info = stock.info

    print("/nCompany Information")
    print("-"* 40)
    
    print(f"Company: {info.get('longName', 'N/A')}")
    print(f"Sector: {info.get('sector', 'N/A' )}")
    print(f"Country: {info.get('country', 'N/A')}")
    print(f"Market Cap: {info.get('marketCap', 'N/A')}")
    print(f"Current Price: {info.get('currentPrice', 'N/A')}")
    print(f"P/E Ratio: {info.get('trailingPE', 'N/A')}")