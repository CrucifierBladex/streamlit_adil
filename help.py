import streamlit as st
import yfinance as yf
import pandas as pd
st.write("""
# Stock Price App APPLE

Stocks are shown below
""")
tickerSymbol='AAPL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start='2010-5-31',end='2021-5-17')
st.write("""
# Closing Price	""")
st.line_chart(tickerDf.Close)
st.write("""
# Volume Price	""")
st.line_chart(tickerDf.Volume)
st.write("""
# Opening Price	""")
st.line_chart(tickerDf.Open)
