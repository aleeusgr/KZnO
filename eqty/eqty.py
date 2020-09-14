#!bin/python

# new functionality:

import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import tx,ty
import numpy as np

try:
    dataX = tx.load_local()
except:
    tx.fetch()
    dataX = tx.load_local()

dataY = ty.load_y() # np.array(23,12), Jan1998 : Dec2020

train_x = dataX['rub'].iloc[1:,1:]['Close'].to_numpy()[:-1] # check if the dates are right
train_x = np.nan_to_num(train_x, nan=27) 
train_y = dataY.reshape(-1)[12*(2004-1998):-4] # Jan'04: Aug'20 
adjst_usd = np.multiply(train_y,1/train_x)

def heatmap(plot,init_year=2004,title ='profit'):
    ''' input: 1D np.array
    DO:
    ??
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    import calendar
    length_years = 2021 - init_year

    # fit the data to 12byN grid
    plot = plot.reshape(1,-1)  
    plot = np.append(plot,np.ones(12-plot.shape[1]%12))
    plot = plot.reshape((length_years,12)) 

    plt.figure(figsize=(20,10))
    plt.title(title)
    plt.yticks(np.arange(12),labels = [calendar.month_abbr[i] for i in range(1,13)])
    plt.xticks(np.arange(length_years),list(range(init_year,2021)))
    plt.imshow(plot.T)
    plt.show()

heatmap(train_y)
heatmap(adjst_usd,title='value in USD')
