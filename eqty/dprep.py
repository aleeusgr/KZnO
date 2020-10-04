#!bin/python
''' Procedures to transform the data:
X: loaded automatically
DO: functionality to choose provider and tickers. low priority
Y: index broken, what happened? cleaned old csv's?


return (train_x,train_y,test_x,test_y)'''

# new functionality:
# TODO: 

import matplotlib.pyplot as plt
import datetime as dt
#import pandas as pd
import tx,ty, visualisation as vis
import numpy as np

dataX = tx.loadX(save_locally=True)
dataY = ty.loadY() # np.array(23,12), Jan1998 : Dec2020
#vis.plot_array(dataY,init_year=1998) init_year needs fixing
# 
# train_x and train_y date alignment:
init_date = dt.date.fromisoformat(dataX.iloc[0,0]) # depends on choice of tickers
train_end_date = dt.date.fromisoformat('2020-08-30')# manuallys set from train_y original source
xy_end_diff = train_end_date-dt.datetime.today().date()
extra_months = xy_end_diff.days//30+1 

# write tests to compare dates here and in the original source:
train_x = dataX.iloc[:extra_months,1:].to_numpy() 
train_y = dataY.reshape(-1)[-1+extra_months+12*(init_date.year-1998)+init_date.month:-4] #this migth break

# Scatterplots:
df = dataX.iloc[:extra_months,:].copy()
df['Y'] = train_y.tolist()
df['Y$'] = df['Y'] / df['rub']
#im = plt.matshow(df.corr(),interpolation='none', vmin=0, vmax=1, aspect='equal')

# There was an example of this in one of the tutorials, check HandsOn ML
import itertools
l = list(itertools.combinations(df.drop('Date',axis=1).columns, 2))
for i in l:
    df.plot(x=i[0],y=i[1],kind='scatter',c=df.index)
    plt.show()
