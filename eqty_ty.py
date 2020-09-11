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


volume = df.iloc[50:96:2,:].copy().reset_index(drop=True)
profit = df.iloc[ 2:47:2,:].copy().reset_index(drop=True)

def visualise(df):
    plot = df.iloc[0:,1:].to_numpy()
    plot = plot.astype(float)

    import matplotlib.pyplot as plt
    import calendar
    plt.figure(figsize=(20,10))
    plt.yticks(np.arange(12),labels = [calendar.month_abbr[i] for i in range(1,13)])
    plt.xticks(np.arange(23),list(range(1998,2021)))

    plt.imshow(plot.T)
    plt.show()

# transform into dataframe, parse dates
df = volume
data = df.iloc[:,1:].to_numpy().reshape(276).astype(float)
 
