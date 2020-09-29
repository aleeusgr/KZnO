#!bin/python
''' Procedures to transform the data:
X: loaded automatically
DO: functionality to choose provider and tickers. low priority
FIX: Somewhere data is not imputed properly, and this messes up imported data!!!!
Y: move to tx.py, rename tx.py to data.py? NO! keep modules small


return (train_x,train_y,test_x,test_y)'''

# new functionality:
# TODO: 

#import matplotlib.pyplot as plt
#import datetime as dt
#import pandas as pd
import tx,ty, visualisation as vis
#import numpy as np

dataX = tx.loadX()
dataY = ty.loadY() # np.array(23,12), Jan1998 : Dec2020
vis.plot_array(dataY,init_year=1998)
# get first init_yearX, init_month_X, 
# X -> train_x (np.array)
# Y -> train_y : procedure to cut the array. use init_year_X, init_month_X
# 

