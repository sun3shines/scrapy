# -*- coding: utf-8 -*-

import os
import fcntl
import shutil
from fastscrapy.globalx.static import ST_DIR
import syslog

class FSt:

    def __init__(self,st):
        self.st = st

    def put(self):
        if self.st.ancestor:
            self.load()
        if not os.path.exists(self.st.path):
            os.mkdir(self.st.path)

    def delete(self):
        os.rmdir(self.st.path)
        
    def error(self,pid,msg):
        pass
    
    def lock(self,incr):
        
        with open(self.st.lock,'r+') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            counter = int(f.readline().split('worker')[0])
            self.erro('counter before: ',str(counter))
            if incr:
                if counter < self.st.total:
                    counter = counter + 1
                else:
                    return False 
            else:
                if counter > 1:
                    counter = counter - 1
                else:
                    return False
                
            f.seek(0)
            f.write(str(counter)+'worker')
            self.error('counter after: ',str(counter))
            return True

    def decr(self):
        return self.lock(False)
        
    def incr(self):
        return self.lock(True)

    def load(self):
        if not os.path.exists(ST_DIR):
            os.mkdir(ST_DIR)
        
        if not os.path.exists(self.st.root):
            os.mkdir(self.st.root)    

        with open(self.st.lock, "w") as f: 
            f.write("1worker") 

    @property
    def empty(self):
        return 0== len(os.listdir(self.st.path))

    @property
    def count(self):   
        return len(os.listdir(self.st.path)) 
 
    @property
    def level(self):
        return (len(self.st.path.split('/'))-1) 

    def erro(self,pid,msg):
        syslog.syslog(syslog.LOG_ERR,'erro process: '+pid +'  '+str(msg))
               
class senateFSt:
    def __init__(self,c):
        
        self.parent = c.parent
        self.pid = c.pid
        self.total = c.total

        self.path = self.root = self.lock = ''

    @property
    def ancestor(self):
        return self.root == self.path
    
    def load(self):
        self.path = '/'.join([self.parent,self.pid])
        self.root = '/'.join(self.path.split('/')[:3])
        self.lock = '/'.join([self.root,'lock'])
    
# 设计思想，就是枪弹分离，有抢无弹，有弹无抢了。    
