#!/bin/python

def loadY(src='prft',verb=False):
    '''Load private history data data
    do: 
    returns: dataY, np.array(23,12)'''
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

    data={
    'vol' : df.iloc[50:96:2,:].copy().reset_index(drop=True),
    'prft': df.iloc[ 2:47:2,:].copy().reset_index(drop=True)
    }
    
    if verb:
        print(data[src])

    # transform into dataframe, parse dates
    df = data[src]
    return df.iloc[:,1:].to_numpy().reshape((23,12)).astype(float)
     
