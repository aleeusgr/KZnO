#!/bin/python

import os
import vk_api
import networkx as nx
import matplotlib.pyplot as plt
import vk as v
import pandas as pd

vk = v.auth() #authentificate and instantiate
#groups = v.my_Groups(vk)
#members = v.get_users(vk)
# TODO:
# graph visualisation: TACTICOOL-related groups, their users, bipartite graph. 
# Data extraction task: consumer target group ID and social media presence. 




#
#
#v.save(members)

data = v.load()


dataset = []
del(data[80958631])
G = nx.from_dict_of_lists(data)
#G = nx.Graph()
#G.add_nodes_from(dataset)
print(G.nodes)
#nx.draw(G)
#plt.show()
