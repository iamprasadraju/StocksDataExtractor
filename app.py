import streamlit as st
from middleware.StockInfo import FetchSymbols
from middleware.StockInfo import FetchStockData 
import yfinance as yf

st.title("📊 Stocks Data Extractor")

query = st.text_input("", placeholder = "Search for a stock symbol or name: ")

if query:
	results = list(FetchSymbols(query))
	
	if not results:
		st.warning("No results found!")
		
	else:
		options = {f"{info[0]}. {info[1]} - {info[2]} ({info[3]})" : info[1] for info in results}
		
		get_symbol = st.radio("select a stock", list(options.keys()), index=None)
		
		if get_symbol:
			# Gets symbols from selected radio button
			selected_symbol = options[get_symbol]
			st.write("You selected symbol:", selected_symbol)
			
			# Fetchs Fundamental stock data
			fundamental_data = FetchStockData(selected_symbol)
			
			st.subheader("🏢 Company & Fundamental Data")
			st.json(fundamental_data)
            
			duration_options = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "ytd", "max"]
			selected_duration = st.selectbox("Select time period:", duration_options)
			
			stock_data = yf.download(selected_symbol, period=selected_duration)
			
			if stock_data.empty:
				st.warning("No data available for this symbol and duration.")
			else:
				# --- Show stock data ---
				st.subheader("📈 Stock Data Preview")
				st.dataframe(stock_data)
				
				# --- Download button ---
				csv_data = stock_data.to_csv().encode("utf-8")
				st.download_button(
				label="📥 Download stock data",
				data=csv_data,
				file_name=f"{selected_symbol}_{selected_duration}.csv",
				mime="text/csv"
				)
				
				# --- Optional: Line chart ---
				st.subheader("📊 Stock Price Chart")
				st.line_chart(stock_data['Close'])