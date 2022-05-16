from helpers.user import generate_user_info
import random
import os
from os import listdir
from os.path import isfile, join
import time

def get_acc_info():
    try:
        with open(os.getcwd() + "\\inputs\\names.txt", "r") as file:
            data = file.read()
            users = data.split("\n")
            data = []
            for user in users:
                user = generate_user_info(user)
                images = [f for f in listdir('images') if isfile(join('images', f))]
                index = random.randint(0,len(images)-1)
                image = os.path.abspath(os.getcwd()) + '\images\\' + images[index]
                user['img'] = image
                data.append(user)
    except:
        print('names.txt file not found')
        exit()
    return data

def get_sites():
    try:
        with open(os.getcwd() + "\\inputs\\websites.txt", "r") as file:
            data = file.read()
            list = data.split("\n")
            data = []
            for site in list:
                data.append(site)
    except:
        print('websites.txt file not found')
        exit()
    return data

def get_proxies():
    try:
        with open(os.getcwd() + "\\inputs\\proxies.txt", "r") as file:
            data = file.read()
            list = data.split("\n")
            data = []
            for site in list:
                data.append(site)
    except:
        print('websites.txt file not found')
        exit()
    return data

def formatted_time(t, hours = False):
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    if hours:
        return '{:d}:{:02d}:{:02d}'.format(h, m, s)
    else: 
        return '{:02d}:{:02d}'.format(m, s)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) 
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Waiting is over')
