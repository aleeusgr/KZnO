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

def write_log():
    with open('log.txt','r+') as f:
       import datetime
       f.write(str(datetime.date.today()))

def check_log():
    with open('log.txt') as f:
        for line in f:
            pass
        last = line
    import datetime
    if datetime.datetime.strptime(last, '%Y-%m-%d').date()==datetime.date.today():
        return False
    else:
        return True

weekdays = [1,3]
if check_date(weekdays) and check_log():
    v = vk.auth()
    pic = choose_pic(newpath)
    result = vk.post_pic(v,pic)
    print(result)
    write_log()
    shutil.move('./{}/{}'.format(newpath,pic),'./{}/{}'.format(oldpath,pic))
    

check_log()
