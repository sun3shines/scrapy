# -*- coding: utf-8 -*-

import json
import os
import fcntl 
import os, time
 
def listattrs(path,r=True):
    
    count = 0
    for obj in os.listdir(path):
        fullpath = '/'.join([path,obj])
        if os.path.isdir(fullpath):
            if r:
                count = count + listattrs(fullpath, r)
            count = count + 1
    return count




def initlock(lockpath):
    
    with open(lockpath, "w") as f: 
        f.write("1") 

def getlock(lockpath,limit):

    flag = False
    with open(lockpath,'r+') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        counter = int(f.readline())
        if counter < limit:
            counter = counter + 1
            f.seek(0)
            f.write(str(counter))
            flag = True
        
    return flag

if __name__ == '__main__':

    print listattrs('/scrapy')
