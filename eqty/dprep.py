#!bin/python
def load_and_process(verbose = True):
    ''' Procedures to transform the data:
    X: loaded automatically
    DO: functionality to choose provider and tickers. low priority
    Y: not sure if indexing works properly, need testing

    return (train_x,train_y,test_x,test_y)'''

    # new functionality:
    # TODO: 

    import matplotlib.pyplot as plt
    import datetime as dt
    #import pandas as pd
    import tx,ty, visual as vis
    import numpy as np

    dataX = tx.loadX(save_locally=True)
    dataY = ty.loadY() # np.array(23,12), Jan1998 : Dec2020

    if verbose:
        pass
        vis.plot_heatmap(dataY,init_year=1998)# tick labelling needs fixing
     
    # train_x and train_y date alignment:
    init_date = dt.date.fromisoformat(dataX.iloc[0,0]) # depends on choice of tickers
    train_end_date = dt.date.fromisoformat('2020-08-30')# manuallys set from train_y original source
    xy_end_diff = train_end_date-dt.datetime.today().date()
    extra_months = xy_end_diff.days//30+1 # this will glitch

    # write tests to compare dates here and in the original source:
    train_x = dataX.iloc[:extra_months,1:].to_numpy() 
    train_y = dataY.reshape(-1)[-1+extra_months+12*(init_date.year-1998)+init_date.month:-4] #this migth break

    # feature extraction
    df = dataX.iloc[:extra_months,:].copy()
    df['Y'] = train_y.tolist()
    df['Y$'] = df['Y'] / df['rub']
    
    if verbose:
        df.hist()
    #vis.scatter(df)

    test_x, test_y = None, None
    
    return train_x,train_y,test_x,test_y
