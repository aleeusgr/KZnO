#!bin/python

# new functionality:

import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import tx,ty

try:
    dataX = tx.load_local()
except:
    tx.fetch()
    dataX = tx.load_local()

dataY = ty.load_y() # np.array(23,12), Jan1998 : ??2020

# dataX['rub']: convet to (Y,M) np.array
# dataY - convert to $, visualise 
# 
