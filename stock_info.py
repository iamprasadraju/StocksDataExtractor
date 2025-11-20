import yfinance as yf
import json

def FetchSymbols(query):
	ticker = yf.Lookup(query)
	df = ticker.stock.reset_index()
	symbols = df.loc[df.exchange == "NSI", "symbol"].tolist()

	for i, symbol in enumerate(symbols):
		ticker = yf.Ticker(symbol)
		data = ticker.info
		print(f"\n{i+1} ===== ", symbol, " =====")
		print("Company Name:", data["shortName"])
		print("Industry:", data["industry"])
		print("====================================\n")
		
	
def FetchStockData(symbols):
	tickers = yf.Tickers(" ".join(symbols))

	for symbol in symbols:
		ticker = tickers.tickers[symbol]
		info = ticker.get_info()
		try:
			print("\n===== ", symbol, " =====")
			print("Company Name:", info.get("shortName"))
			print("Website URL:", info.get("website"))
			print("Industry:", info.get("industry"))
			print("About Company:", info.get("longBusinessSummary"))
			print("Employees Count:", info.get("fullTimeEmployees"))
			print("Market Cap:", info.get("marketCap"), info.get("currency"))
			print("Current Share Price:", info.get("currentPrice"))
			print("====================================\n")
		except KeyError as e:
			print(e)
	return ""



query = input("Query: ")
FetchSymbols(query)