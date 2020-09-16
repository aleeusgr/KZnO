#!/bin/python

import os
import vk_api
import networkx as nx
import matplotlib.pyplot as plt
import vk as v
import pandas as pd

vk = v.auth() #authentificate and instantiate
# TODO:
# graph visualisation: TACTICOOL-related groups, their users, bipartite graph. 
# Data extraction task: consumer target group ID and social media presence. 

#my_group_ids = vk.groups.get()['items']
#usr_list = v.scrape_users_in_my_groups(my_groups)
#dataset = v.scrape_groups()

my_groups = v.load()

tactic = pd.DataFrame(my_groups).loc[[0,1,2,6,11,13,18,19,20,22,23]]


#v.save(dataset)
dataset = []

G = nx.Graph()
G.add_nodes_from(dataset)
print(G.nodes)
#nx.draw_circular(G)
#plt.show()
