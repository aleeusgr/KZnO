#!bin/python
''' Procedures to transform the data:
X: loaded automatically
DO: functionality to choose provider and tickers. low priority
Y: move to tx.py, rename tx.py to data.py? NO! keep modules small


return (train_x,train_y,test_x,test_y)'''

# new functionality:
# TODO: 

#import matplotlib.pyplot as plt
import datetime as dt
#import pandas as pd
import tx,ty, visualisation as vis
#import numpy as np

dataX = tx.loadX(save_locally=True)
dataY = ty.loadY() # np.array(23,12), Jan1998 : Dec2020
#vis.plot_array(dataY,init_year=1998)
# 
train_x = dataX.iloc[:,1:].to_numpy() #CHECK for the end date
init_date = dt.date.fromisoformat(dataX.iloc[0,0])
train_y = dataY.reshape(-1)[-1+12*(init_date.year-1998)+init_date.month:-4] # FIX SHAPE!
#import tensorflow as tf

