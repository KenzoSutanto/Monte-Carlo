import yfinance as yf
import pandas as pd
import numpy as np

data = (yf.download("BLK",period="max",interval="1d",auto_adjust=False))

data["Returns"] = data["Adj Close"].pct_change()
data["Last Price"] = data["Adj Close"].iloc[-1] 
print(data.head())

