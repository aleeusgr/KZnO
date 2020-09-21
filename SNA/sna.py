#!/bin/python
'''
# TODO:
# graph visualisation: TACTICOOL-related groups, their users, bipartite graph. 
# Do small ideas, play around, combine.
# Try: show only groups, but size is proportional to a metric. Going deeper - research several metrics.
# 
# * node coding: size, color.
# Data extraction ideas:
* identify social network cluster: BDB

'''
import os
import vk_api
import networkx as nx
import matplotlib.pyplot as plt
import vk as v
import pandas as pd

#vk = v.auth() #authentificate and get and instance of vk_api 
#groups = v.my_Groups(vk)
#members = v.get_users(vk)
#v.save(members)

data = v.load()

G = nx.from_dict_of_lists(data)
#G = nx.Graph()
#print(G.nodes)
#nx.draw(G)
#plt.show()
