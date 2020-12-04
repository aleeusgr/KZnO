#!/bin/python

import os
import vk_api
import networkx as nx
import matplotlib.pyplot as plt

def auth():
    '''
    TODO: token + login and pass + login
    get cred by "echo '<login> <pass>' >> cred
    '''
    with open('vk_cred') as f:
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


def post_pic(vk,pic, group_id = 143352934):
    ''' post a photo to a group wall, 
    achieved by a combination of 3 API methods: upload, save, post to wall,
    vk:API instance, returned by vk.auth()
    pic: str, name
    group_id: int, >0
    '''

    import requests
    
    workdir = 'fresh'
    url = vk.photos.getWallUploadServer(group_id = group_id)['upload_url']
    print(url)
    #url = 'https://httpbin.org/post'

    # need to post as multipart/form-data
    files = {'file': open('./{}/{}'.format(workdir,pic), 'rb')}
    response = requests.post(url, files=files)
    server = int(response.json()['server'])
    photo = response.json()['photo']
    hsh = response.json()['hash']
    response.close()

    save = vk.photos.saveWallPhoto(group_id = group_id,server = server, photo = photo, hash = hsh)

    my_id = save[0]['owner_id']
    return vk.wall.post(owner_id = -1*group_id, from_group = 1, attachments = 'photo{}_{}'.format(my_id, save[0]['id']))
