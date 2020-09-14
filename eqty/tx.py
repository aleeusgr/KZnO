#!bin/python

def fetch(resample='1M'):
    '''Get data from web
     DO:
     try different sources
     parameters 

     resamples, saves to disk'''

    import pandas_datareader.data as web
    import datetime as dt
    import world_bank_data as wb

    #wb.get_topics()

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
    web_data = {
    'oil' : web.DataReader('CL=F',provider[0],start,end) ,
    'rub' : web.DataReader('RUB=X',provider[0],start,end) 
    }
    dataM={}
    for i in web_data.keys():
        dataM[i] = web_data[i].resample(resample).mean()
        dataM[i].to_csv('{}.csv'.format(i))

def load_local():
    '''Load local data
    DO:auto read all csv in the folder?'''
    import pandas as pd
    data = {
    'oil' : pd.read_csv('oil.csv'),
    'rub' : pd.read_csv('rub.csv')
    }
    
    #
    # Feature extraction ideas: Indicator from normalized world index values. provider[4]

    return data
    #return data['rub'].iloc[1:,1:].to_numpy()

def show_train_x_graphs():

    oil = pd.read_csv('oil.csv')
    rub = pd.read_csv('rub.csv')

    plt.figure(figsize=(10,5))
    plt.plot(oil['Close'],label='Crude Oil')
    plt.plot(rub['Close'],label='USD/RUB')
    plt.legend()
    plt.show()

