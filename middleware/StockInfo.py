import yfinance as yf
import json

def FetchSymbols(query):
	ticker = yf.Lookup(query)
	df = ticker.stock.reset_index()
	symbols = df.loc[df.exchange == "NSI", "symbol"].tolist()

	for i, symbol in enumerate(symbols):
		ticker = yf.Ticker(symbol)
		data = ticker.info
		Name = data.get("shortName", "N/A")
		Industry = data.get("industry", "N/A")
		
		yield [i+1,symbol, Name, Industry]

def FetchStockData(symbols):
    tickers = yf.Tickers(" ".join(symbols))
    all_data = []

    for symbol in symbols:
        ticker = tickers.tickers[symbol]
        info = ticker.get_info()
        
        # Store data in a dictionary
        stock_data = {
            "Symbol": symbol,
            "Company Name": info.get("shortName", "N/A"),
            "Current Price": info.get("currentPrice", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "PE Ratio (TTM)": info.get("trailingPE", "N/A"),
            "Forward PE": info.get("forwardPE", "N/A"),
            "Price to Book": info.get("priceToBook", "N/A"),
            "Price to Sales": info.get("priceToSalesTrailing12Months", "N/A"),
            "Revenue Growth (YoY)": info.get("revenueGrowth", "N/A"),
            "Earnings Growth (YoY)": info.get("earningsGrowth", "N/A"),
            "Profit Margin": info.get("profitMargins", "N/A"),
            "Operating Margin": info.get("operatingMargins", "N/A"),
            "ROE": info.get("returnOnEquity", "N/A"),
            "ROA": info.get("returnOnAssets", "N/A"),
            "Total Debt": info.get("totalDebt", "N/A"),
            "Total Cash": info.get("totalCash", "N/A"),
            "Operating Cash Flow": info.get("operatingCashflow", "N/A"),
            "Book Value Per Share": info.get("bookValue", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A"),
            "Dividend Rate": info.get("dividendRate", "N/A"),
            "Payout Ratio": info.get("payoutRatio", "N/A"),
            "52-Week Range": info.get("fiftyTwoWeekRange", "N/A"),
            "52-Week Low": info.get("fiftyTwoWeekLow", "N/A"),
            "52-Week High": info.get("fiftyTwoWeekHigh", "N/A"),
            "50-Day Avg Price": info.get("fiftyDayAverage", "N/A"),
            "200-Day Avg Price": info.get("twoHundredDayAverage", "N/A"),
            "Volume": info.get("volume", "N/A"),
            "Avg Volume (3M)": info.get("averageDailyVolume3Month", "N/A"),
            "About Company": info.get("longBusinessSummary", "N/A")
        }

        all_data.append(stock_data)

    return all_data
