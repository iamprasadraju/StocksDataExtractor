import requests
import json


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
		
print(fetch_symbol("ola"))
