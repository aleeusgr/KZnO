#!bin/python

# new functionality:
# TODO: 
# clean: functions in modules, only experimental functionality in main.
# import sklearn, remember regression methods. SGD, Boost, Ensemble?? 

import dprep  

tr_x,tr_y,ts_x,ts_y = dprep.load_and_process(verbose=False)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler

num_pipeline = Pipeline([
    #('std_scaler', StandardScaler()),
    ('min_max', MinMaxScaler()),
    ])

scaled = num_pipeline.fit_transform(tr_x)

# model selection

