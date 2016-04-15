# -*- coding: utf-8 -*-

import json
import os
import fcntl 
import os, time
from fastscrapy.worker.core.log import logerror
 
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
    
#    with open(lockpath, "w") as f: 
#        f.write("1worker") 
    pass
def incrlock(lockpath,limit):

#    flag = False
#    with open(lockpath,'r+') as f:
#        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
#        counter = int(f.readline().split('worker')[0])
#        logerror('incr counter before: ',str(counter))
#        if counter < limit:
#            counter = counter + 1
#            f.seek(0)
#            f.write(str(counter)+'worker')
#            logerror('incr counter after: ',str(counter))
#            flag = True
        
#    return flag
    pass

def decrlock(lockpath,limit):

#    flag = False
#    with open(lockpath,'r+') as f:
#        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
#        counter = int(f.readline().split('worker')[0])

#        logerror('decr counter before: ',str(counter)) 
#        if counter > 1:
#            counter = counter - 1
#            f.seek(0)
#            f.write(str(counter)+'worker')
#            logerror('decr counter after: ',str(counter))
#            flag = True

#    return flag
    pass    

if __name__ == '__main__':

    print listattrs('/scrapy')
