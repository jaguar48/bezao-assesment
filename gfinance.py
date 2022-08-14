import pandas_datareader as data
import pandas as pd

tickers = ['tsla', 'btc-usd', 'goog', 'amzn']

sf = data.DataReader(tickers, data_source='yahoo')

df = pd.DataFrame(sf)
print (df.sum())
