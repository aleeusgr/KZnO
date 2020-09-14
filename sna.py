#!/bin/python

import os
import vk_api

def auth():
    vk_session = vk_api.VkApi('+79202720942')
    vk_session.auth(token_only=True)
    return vk_session.get_api()

vk = auth()

friend_ids = vk.friends.get() #ids of active user friends
#friends_verbose = vk.users.get(user_ids = friend_ids['items']) # get user info from ids
#users_by_group = vk.groups.getMembers(group_id='zarya71') # get users of a group
my_groups = vk.groups.get()['items']
people_in_groups = {}
for group_id in my_groups:
    group = vk.groups.getById(group_ids=group_id)[0]['name']
    people_in_groups[group] = vk.groups.getMembers(group_id=group_id)
    print(group)

#def group_tested_methods(name = groups[0]):
#    vk.groups.getById(group_ids=name)
#    return vk.groups.getMembers(group_id=name)
#
#def user_tested_methods(names = ('kanaby')): # renam
#    user = vk.users.get(user_ids = names)
#    user_id = user[0]['id']
#    return vk.groups.get(user_id=user_id) 
#    #return  vk.friends.get(user_id = user_id)
#
# NOTES:
# general: framework for VK data mining and exploration
# module: generate a network of friends from list of users
# list of users can come from: users, groups, ???
# 
# 
