import yfinance as yf
import json
import os


# Period '1mon' is invalid, must be one of: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, ytd, max")



def SaveAsCSV(symbols, period = "1mo"):
	try:
		os.mkdir("csv")
	except:
		pass
	for symbol in symbols:
		df = yf.download(symbol, period = period)
	
		filename = symbol[:-3]
		df.to_csv(f"csv/{filename}.csv")



SaveAsCSV(["TITAN.NS", "OLAELEC.NS"])
