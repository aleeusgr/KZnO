#!/bin/python

import pandas as pd
from pathlib import PosixPath

#PATH = PosixPath('/home/alex/HDD/workshop/.datasets/KZnO/1.xls') 
PATH = '/home/alex/HDD/workshop/.datasets/KZnO/2.xls'

# read the format properly
df = pd.read_excel(PATH,verbose=True,sheet_name='данные',
                    usecols=(range(13)),
                    header=0,
                    na_values=[' ']).fillna(0)
df.columns = (range(13))

print(df.iloc[2::2,:].head())
print(df.iloc[2::2,:])

# split df into ranges:
# print full 
# find slices for sections.

