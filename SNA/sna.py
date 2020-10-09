#!/bin/python
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
    DO: make colors representative
     
    returns None'''
    pos = nx.spring_layout(G, iterations=20)
    ubd = util.users_by_degree(G)
    for rank in ubd: 
        #G1 = nx.subgraph(G,ubd[rank])
        #nx.draw_networkx_nodes(G,pos,ubd[rank], rank*75,node_color=range(len(ubd[rank])),cmap='seismic')
        nx.draw_networkx_nodes(G,pos,ubd[rank], node_color=rank,cmap='seismic')
    plt.show()
