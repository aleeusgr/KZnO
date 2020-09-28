# KZnO

## eqty 
### v0.1 Data 
X must be a normalized dataset. In tx set accordingly: 
* full range of data is loaded, shortest dataset ID'd and all are resampled and saved in a single pd.DataFrame()
* dprep will fetch\read. Rewrite ty cutting procedure to take first and last date from dataX as cut points for dataY
* Visualisation function will get broken. Fix, move to the separate module. Desired functionality: take a pd.Series or np.array as input, fit it to 12byN plot and visualise. 
### v0.2 Model
* Regression task  
* try TFCoder functionality?
* GridCV??
* Play with train_x

#### v0.3 Predictive performance

## sna
#### v0.1: graph generation from vk data.
MEM: 
SNA$ echo 'name pass' >> cred

vk.py: rename 	
#### v0.2: 
ideas on graph vis:
* color coding: group/user; how to use cmaps?
* size: centrality, degree, whatever. 

What information from the graph I can use?
Task: from the sample obtain key figures:
* node centrality.
* number of steps for signal to reach all nodes.
* graph partitioning 
