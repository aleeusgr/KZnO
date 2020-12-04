import vk
import requests
import shutil

newpath  = 'fresh'
oldpath = 'used'

def choose_pic(path):
    import os
    import random
    pic = random.choice(os.listdir(path))
    return pic

def check_date(weekdays):
    import datetime
    today = datetime.datetime.today().weekday()
    if today in weekdays:
        return True
    else:
        print(today)
        return False


weekdays = [1,3]
if check_date(weekdays):
    v = vk.auth()
    pic = choose_pic(newpath)
    result = vk.post_pic(v,pic)
    print(pic)
    shutil.move('./{}/{}'.format(newpath,pic),'./{}/{}'.format(oldpath,pic))
    
    



