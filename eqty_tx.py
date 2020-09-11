#!bin/python

import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

provider = {
0:'yahoo',  # symbols: MSFT
1:'quandl', #has specific symbol format. symbols:??? 
2: 'moex',  #Moscow Exchange.  symbols:??? 
3: 'fred',  #???
4: 'stooq', #common index data. symbols: ^DJI
5: 'eurostat', #browse website for symbols
6: 'iex',   # requires API key
}

def fetch():
    start = '1998-01-01'
    end = None
    web_data = {
    'oil' : web.DataReader('CL=F',provider[0],start,end) ,
    'rub' : web.DataReader('RUB=X',provider[0],start,end) 
    }
    dataM={}
    for i in web_data.keys():
        dataM[i] = web_data[i].resample('1M').mean()
        dataM[i].to_csv('{}.csv'.format(i))

#fetch()


data = {
'oil' : pd.read_csv('oil.csv'),
'rub' : pd.read_csv('rub.csv')
}

#
# Feature extraction ideas: Indicator from normalized world index values. provider[4]

