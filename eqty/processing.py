#!bin/python

# write a procedure to automate pre-processing. 
#
import tx
#tx.fetch()

# write procedure to fetch train and test separetly

dataX = tx.load_local_x()
def processing(dataX):    
    '''returns np array?? '''
    for idx,dset in dataX.items():
        print(len(dset),idx)
        ##Impute missing values:
        ##dset.fillna(method='bfill',inplace=True)
        #print(dset)
        ## Cut data to smallest dataset:
        ###print(dset.loc[:,'Date'].min())
        ###print(dset.iloc[1:,1:]['Close'].to_numpy().shape)#[:-1]) 
        ##print(dset.iloc[len(dset)-shortest:,1:]['Close'].to_numpy().shape)#[:-1]) 

    #print(dataX)
    return None

processing(dataX) 
