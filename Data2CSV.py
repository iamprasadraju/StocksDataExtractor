import yfinance as yf
import json



def extract_data(symbols):
	df = yf.download(symbols, group_by="ticker")
	print(df)
	df.to_csv("out.csv")



extract_data(["TITAN.NS", "OLAELEC.NS"])
