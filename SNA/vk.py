#!/bin/python

import os
import vk_api
import networkx as nx
import matplotlib.pyplot as plt

def auth():
    '''
    get cred by "echo '<login> <pass>' >> cred
    '''
    with open('cred') as f:
       cred = f.read().split() 
    import vk_api
    vk_session = vk_api.VkApi(cred[0])
    vk_session.auth(token_only=True)
    return vk_session.get_api()


def save(dataset,outputFile = 'test.data'):
    import pickle 
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()

def load(inputFile = 'test.data'):
    import pickle
    fd = open(inputFile, 'rb')
    return pickle.load(fd)

def my_Groups(vk):
    '''vk: returned by auth()
        returns (group_id,'GroupName')'''
    my_groups=[]
    for group_id in vk.groups.get()['items']:
        my_groups.append((group_id, vk.groups.getById(group_ids=group_id)[0]['name']))
    return my_groups
    
def get_group_members(vk):
    '''vk: returned by auth()
        returns {<group_id>:[groups_users]}
        '''
    import pandas as pd
    my_groups = vk.groups.get()['items']
    relevant = pd.DataFrame(my_groups).loc[[0,1,2,6,11,13,18,19,20,22,23]]
    id_list= relevant.iloc[:,0].to_list()
    users={}
    for i in id_list:
        try:
            users[i] = vk.groups.getMembers(group_id=i)['items']
        except:
            pass
            #users[i] = i
    return users

def load_dataset(save_locally = True):
    try:
        data = load()
    except:
        vk = v.auth() #authentificate and get and instance of vk_api 
        data = v.get_users(vk)
        if save_locally:
            v.save(data)
    return data
