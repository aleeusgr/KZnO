#!/bin/python

import os
import vk_api
import networkx as nx
import matplotlib.pyplot as plt

def auth():
    with open('cred') as f:
       cred = f.read().split() 
    import vk_api
    vk_session = vk_api.VkApi(cred[0])
    vk_session.auth(token_only=True)
    return vk_session.get_api()


#friends_verbose = vk.users.get(user_ids = friend_ids['items']) # get user info from ids
#users_by_group = vk.groups.getMembers(group_id='zarya71') # get users of a group
#my_groups = vk.groups.get()['items']

def save(dataset,outputFile = 'test.data'):
   
    import pickle 
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()

def load(inputFile = 'test.data'):
    import pickle
    fd = open(inputFile, 'rb')
    return pickle.load(fd)

def scrape_group_names():
    '''Returns (group_id,'GroupName')'''
    my_groups=[]
    for group_id in vk.groups.get()['items']:
        my_groups.append((group_id, vk.groups.getById(group_ids=group_id)[0]['name']))
    return my_groups
    
def scrape_users_in_my_groups(my_groups):
    '''returns {group_id:(groups users)}'''
    people_in_groups = {}
    for group_id in my_groups:
        #group = vk.groups.getById(group_ids=group_id)[0]['name']
        try:
            people_in_groups[group_id] = vk.groups.getMembers(group_id=group_id)
        except:
            people_in_groups[group_id] = 'error'
    return people_in_groups

#def group_tested_methods(name = my_groups[0]):
#    vk.groups.getById(group_ids=name) #gets group info
#    return vk.groups.getMembers(group_id=name)
#
#def user_tested_methods(names = ('kanaby')): # renam
#    user = vk.users.get(user_ids = names)
#    user_id = user[0]['id']
#    return vk.groups.get(user_id=user_id) 
#    #return  vk.friends.get(user_id = user_id)
#    vk.friends.get() #ids of active user friends
