#!/bin/python

import os
import vk_api

vk_session = vk_api.VkApi('+79202720942')
vk_session.auth(token_only=True)
vk = vk_session.get_api()


friend_ids = vk.friends.get() #ids of active user friends
#friends_verbose = vk.users.get(user_ids = friend_ids['items']) # get user info from ids
#users_by_group = vk.groups.getMembers(group_id='zarya71') # get users of a group

#get users friends by username
names = ('kanaby')
user = vk.users.get(user_ids = names)
user_id = user[0]['id']
users_friends_ids = vk.friends.get(user_id = user_id)

# NOTES:
# general: framework for VK data mining and exploration
# module: generate a network of friends from list of users
# list of users can come from: users, groups, ???
# 
# 
