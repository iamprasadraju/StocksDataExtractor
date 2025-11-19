import yfinance as yf
import json

def FetchSymbols(query):
	ticker = yf.Lookup(query)
	df = ticker.stock.reset_index()
	symbols = df.loc[df.exchange == "NSI", "symbol"].tolist()
	return symbols
	
def FetchStockData(symbols):
	tickers = yf.Tickers(symbols)
	for symbol in symbols:
		try:
			ticker = tickers.tickers[symbol]
			data = ticker.info
			
			print("\n===== ", symbol, " =====")
			
			print("Company Name:", data["shortName"])
			print("Website url:", data["website"])
			print("Industry:", data["industry"])
			print("About Company:", data["longBusinessSummary"])
			print("Employees Count:", data["fullTimeEmployees"])
			print("Market Cap:", data["marketCap"], data["currency"])
			print("Current Share Price:", data["currentPrice"])
			print("====================================\n")
			
		except Exception as e:
			print(f"Error fetching data for {symbol}: {e}")
			
symbol = FetchSymbols("bajaj")
FetchStockData(symbol)