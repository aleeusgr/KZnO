#!bin/python

import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

symbol = "CL=F"
provider = {
0:'yahoo',  # symbols: MSFT
1:'quandl', #has specific symbol format. symbols:??? 
2: 'moex',  #Moscow Exchange.  symbols:??? 
3: 'fred',  #???
4: 'stooq', #common index data. symbols: ^DJI
5: 'eurostat', #browse website for symbols
6: 'iex',   # requires API key
}

start = '1998-01-01'
end = None

#data = web.DataReader(symbol,provider[0],start,end) 
def fetch():
    oil = web.DataReader('CL=F',provider[0],start,end) 
    rub = web.DataReader('RUB=X',provider[0],start,end) 
    oil.to_csv('oil.csv')
    rub.to_csv('rub.csv')
#fetch()

oil = pd.read_csv('oil.csv')
rub = pd.read_csv('rub.csv')

df = rub
df.set_index('Date', inplace=True)
df.index = pd.to_datetime(df.index)
df.resample('1M').mean()

# Feature extraction ideas: Indicator from normalized world index values. provider[4]

