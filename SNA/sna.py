#!/bin/python
'''
# TODO:
# graph visualisation: TACTICOOL-related groups, their users, bipartite graph. 
# Do small ideas, play around, combine.
# Try: show only groups, but size is proportional to a metric. Going deeper - research several metrics.
# function to draw graph by steps? 
# What information can I get from these data?
# * node coding: size, color.
# Data extraction ideas:
* identify social network cluster: BDB

'''
import os
import networkx as nx
import matplotlib.pyplot as plt
import vk as v
import pandas as pd
from networkx.algorithms import bipartite

#vk = v.auth() #authentificate and get and instance of vk_api 
#groups = v.my_Groups(vk)
#members = v.get_users(vk)
#v.save(members)

data = v.load()
G = nx.from_dict_of_lists(data)

# add_node_attributes, 
degree_cent = nx.degree_centrality(G)# what are other types and whats the diffrence? degree/total_n_nodes??
degrees = bipartite.basic.degrees(G,G.nodes)
attrib = degree_cent
att_name = 'degree_centr'
nx.set_node_attributes(G,attrib,att_name)

def node_by_number(n):
    node = list(G.nodes)[n]
    print(G.nodes[node][att_name])

# Pandas Dataframe 
#df = pd.Series(attrib,index=G.nodes) #Check if index connects with data. 



groups, users = bipartite.sets(G)

def draw_subgraph(G,sub):
    layout = nx.circular_layout(G)
    #layout = nx.spring_layout(G)
    G = nx.subgraph(G,sub) # separate a subgraph:
    for n in G:
        nx.draw_networkx_nodes(n,layout)
    plt.show()

#draw_subgraph(G,list(users)[:10])
def draw_AB(G):
    '''slow'''
    layout = nx.spring_layout(G)
    for s,n in zip(('green','red'),reversed(bipartite.sets(G))): 
        Gs1 = nx.subgraph(G,n) # separate a subgraph:
        nx.draw_networkx_nodes(Gs1,layout,node_color=s)
    plt.show()

#draw_parts(G)

