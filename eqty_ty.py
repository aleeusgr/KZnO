#!/bin/python

import pandas as pd
from pathlib import PosixPath
import datetime as dt

#PATH = PosixPath('/home/alex/HDD/workshop/.datasets/KZnO/1.xls') 
PATH = '/home/alex/HDD/workshop/.datasets/KZnO/2.xls'


df = pd.read_excel(PATH,sheet_name='данные',
                    usecols=(range(13)),
                    header=0,
                    na_values=[' ']).fillna(0)
df.columns = (range(13))

pd.options.display.max_rows = 100
#print(df.iloc[2::2,:])

vol =  df.iloc[50:96:2,:].copy()
prft = df.iloc[2:47:2,:] .copy()
print(vol)
print(prft)

# transform into dataframe, parse dates
df = pd.DataFrame()
