#!/usr/bin/env python3
import requests
import json

# fectchs symbols from query
def fetch_symbol(query):
	url = "https://nse-api-khaki.vercel.app/search?q=" + query
	response = requests.get(url).json()
	
	if response:
		symbols = []
		num_sym = response["total_results"]
		result = response["results"]
		for i in range(num_sym):
			symbols.append(result[i]["symbol"])
		return symbols

# fectchs stock data using symbol
def fetch_data(symbols):
	sym_url = "https://nse-api-khaki.vercel.app/stock/list?symbols=" + ",".join(symbols) + "&res=num"
	response = requests.get(sym_url).json()
	
	if response:
		#print(json.dumps(response, indent=2))
		count = response["count"]
		
		for i in range(count):
			print(f"Company Name: {response["stocks"][i]["company_name"]} ({response["stocks"][i]["sector"]})")
			print("Exchange:",response["stocks"][i]["exchange"])
			print("Last Price:", response["stocks"][i]["last_price"])
			print("\n")
	else:
		raise ValueError


symbols = fetch_symbol("titan")

Popular_StockSymbols = ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ICICIBANK", "BHARTIARTL", "SBIN", "ITC", "HINDUNILVR", "IOC", "LT", "ASIANPAINT", "MARUTI"]


fetch_data(symbols)





