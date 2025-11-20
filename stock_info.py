#!/usr/bin/env python3

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
		print("Company Name:", data.get("shortName", "N/A"))
		print("Industry:", data.get("industry", "N/A"))
		print("====================================\n")
		
		
def FetchStockData(symbols):
	tickers = yf.Tickers(" ".join(symbols))

	for symbol in symbols:
		ticker = tickers.tickers[symbol]
		info = ticker.get_info()

		print("\n===== ", symbol, " =====")

		print("Company Name:", info.get("shortName", "N/A"))

		# --- PRICE & VALUATION ---
		print("Current Price:", info.get("currentPrice", "N/A"))
		print("Market Cap:", info.get("marketCap", "N/A"), info.get("currency", ""))
		print("PE Ratio (TTM):", info.get("trailingPE", "N/A"))
		print("Forward PE:", info.get("forwardPE", "N/A"))
		print("Price to Book (PB):", info.get("priceToBook", "N/A"))
		print("Price to Sales:", info.get("priceToSalesTrailing12Months", "N/A"))

		# --- GROWTH ---
		print("Revenue Growth (YoY):", info.get("revenueGrowth", "N/A"))
		print("Earnings Growth (YoY):", info.get("earningsGrowth", "N/A"))

		# --- PROFITABILITY ---
		print("Profit Margin:", info.get("profitMargins", "N/A"))
		print("Operating Margin:", info.get("operatingMargins", "N/A"))
		print("Return on Equity (ROE):", info.get("returnOnEquity", "N/A"))
		print("Return on Assets (ROA):", info.get("returnOnAssets", "N/A"))

		# --- FINANCIAL HEALTH ---
		print("Total Debt:", info.get("totalDebt", "N/A"))
		print("Total Cash:", info.get("totalCash", "N/A"))
		print("Operating Cash Flow:", info.get("operatingCashflow", "N/A"))
		print("Book Value Per Share:", info.get("bookValue", "N/A"))

		# --- DIVIDENDS ---
		print("Dividend Yield:", info.get("dividendYield", "N/A"))
		print("Dividend Rate:", info.get("dividendRate", "N/A"))
		print("Payout Ratio:", info.get("payoutRatio", "N/A"))

		# --- TRADING / TREND ---
		print("52-Week Range:", info.get("fiftyTwoWeekRange", "N/A"))
		print("52-Week Low:", info.get("fiftyTwoWeekLow", "N/A"))
		print("52-Week High:", info.get("fiftyTwoWeekHigh", "N/A"))
		print("50-Day Avg Price:", info.get("fiftyDayAverage", "N/A"))
		print("200-Day Avg Price:", info.get("twoHundredDayAverage", "N/A"))
		print("Volume:", info.get("volume", "N/A"))
		print("Avg Volume (3M):", info.get("averageDailyVolume3Month", "N/A"))

		print("====================================\n")

		return ""




symbol = input("Query: ")
FetchStockData([symbol])