#!/bin/python
'''
Ok, I got users sorted by number of groups.
assume target audience of the groups is the same? Should I implement user statistics by group?

FInd method for distance calculation: closer users are easier attracted? 
remove self: which parts of the graph will stay connected?
assign color to degree_centrality?


'''
import os
import networkx as nx
import matplotlib.pyplot as plt
import vk
import pandas as pd
from networkx.algorithms import bipartite
import util

data = vk.load_dataset()
G = nx.from_dict_of_lists(data)
# nx FUNCTIONS:
degree_cent = nx.degree_centrality(G)# what are other types and whats the diffrence? degree/total_n_nodes??
nx.set_node_attributes(G,degree_cent,'degree_centrality')

groups, users = bipartite.sets(G)
 
def draw_by_degree(G):
    '''Super slow
    DO: colors? 
    move to util
     
    returns None'''
    # How to exclude nodes with degree=1 from computation?
    pos = nx.spring_layout(G, iterations=40) # iterations ~ complexity. 
    #pos = nx.circular_layout(G)
    ubd = util.users_by_degree(G)
    for rank in ubd: 
        #G1 = nx.subgraph(G,ubd[rank])
        size = 10 + 10*rank*(rank-1)
        nx.draw_networkx_nodes(G,pos,ubd[rank], size)#,node_color=range(len(ubd[rank])),cmap='seismic')
        #nx.draw_networkx_nodes(G,pos,ubd[rank], node_color=rank,cmap='seismic')
    plt.show()

draw_by_degree(G)
