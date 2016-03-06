# -*- coding: utf-8 -*-

import os

class Proc:
    
    def __init__(self,ppath,pid):
        self.ppath = ppath
        self.pid = pid 
        self.file = '/'.join([self.ppath,pid,'pid'])
        self.dir = '/'.join([self.ppath,pid])
        self.root = '/'.join(self.dir.split('/')[:2])
        self.total = self.bfs = self.dfs = 0
        self.lockpath = '/'.join([self.root,'lock'])
        
    def put(self,t):
        # type 取 dir 或 file        
        if 'dir' == t:
            os.mkdir(self.dir)
        else:
            file(self.file,'w').close()
    
    def delele(self,t):
        if 'file' == t:
            os.remove(self.file)
        else:
            os.rmdir(self.dir)
    
    @property
    def empty(self):
        if 0== len(os.listdir(self.dir)):
            return True
        return False

    @property
    def count(self):   
        return len(os.listdir(self.dir)) 

    def push(self,val):
        pass
    
    def pop(self):
        pass
    
    
        
