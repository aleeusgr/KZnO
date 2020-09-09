#!/bin/python

import pandas as pd
from pathlib import PosixPath
import datetime as dt
import numpy as np

#PATH = PosixPath('/home/alex/HDD/workshop/.datasets/KZnO/1.xls') 
PATH = '/home/alex/HDD/workshop/.datasets/KZnO/2.xls'


df = pd.read_excel(PATH,sheet_name='данные',
                    usecols=(range(13)),
                    header=0,
                    na_values=[' ']).fillna(0)
df.columns = (range(13))

pd.options.display.max_rows = 100
#print(df.iloc[2::2,:])

vol =  df.iloc[50:96:2,:].copy().reset_index(drop=True)
prft = df.iloc[2:47:2,:] .copy().reset_index(drop=True)

##Visualise
##
plot = prft.iloc[0:,1:].to_numpy()
plot = plot.astype(float)

import matplotlib.pyplot as plt
import calendar
plt.figure(figsize=(20,10))
months = [calendar.month_abbr[i] for i in range(1,13)]
plt.yticks(np.arange(12),labels=months)
plt.xticks(np.arange(23),list(range(1998,2021)))

plt.imshow(plot.T)
plt.show()

# transform into dataframe, parse dates
df = pd.DataFrame()
