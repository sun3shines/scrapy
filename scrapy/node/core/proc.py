# -*- coding: utf-8 -*-

import os
import time
import sys
import json

from scrapy.node.core.http import sendurls,sendhrmv,recvconf
from scrapy.node.core.log import logfork,logexit,logerror
from scrapy.node.core.fs import listattrs,initlock,incrlock,decrlock
from scrapy.node.page import getpage

class Proc:
    
    def __init__(self,host,parent):
        self.host = host
        self.parent = parent
        self.pid = str(os.getpid())
        self.dir = '/'.join([self.parent,self.pid])
        self.root = '/'.join(self.dir.split('/')[:2])
        self.lockpath = '/'.join([self.root,'lock'])
        self.path = self.dir
        
        self.finishurls = []
        self.attrs = None
        self.total = self.bfs = self.dfs = 0
        
        
    def put(self):
        os.mkdir(self.dir)
        
    def delele(self):
        os.rmdir(self.dir)
    
    @property
    def empty(self):
        return 0== len(os.listdir(self.dir))

    @property
    def count(self):   
        return len(os.listdir(self.dir)) 

    def create(self):
        
        t = recvconf()
        if 2 != t.status/100:
            logerror(self.pid, 'recv controller config failed .exit.')
            sys.exit(0)
        self.put()
        self.total = int(t.headers.get('total_limit',0))
        self.dfs = int(t.headers.get('dfs_limit',0))
        self.bfs = int(t.headers.get('bfs_limit',0))
        self.inittimes = int(t.headers.get('try_times','3'))
        self.sleep_interval = int(t.headers.get('proc_sleep_interval','5'))
        self.trytimes = self.inittimes
        
    def destroy(self):
        
        sendhrmv(self.host, self.pid)
        self.delele()
        decrlock(self.lockpath,self.total)
        sys.exit(0)

    def fork(self):
        return os.fork()
   
    @property
    def level(self):
        return (len(self.dir.split('/'))-1) 

    @property
    def allow(self):
        return ( self.count <int(self.bfs) and self.level < self.dfs and incrlock(self.lockpath, self.total))
#        return False

    def send(self):
        t = sendurls(self.host, self.pid, self.finishurls)
        if 2 != t.status/100:
            self.reset()
            return False
        else:
            param = t.headers
            self.cmd = param.get('url')
            if self.cmd not in ['wait','stable','speed']:
                self.reset()
                return False
            
            self.attrs = json.loads(t.data)
            return True
    
    def run(self):
        self.trytimes = self.inittimes
        self.finishurls = getpage(self.attrs)
    
    def sleep(self):
        time.sleep(self.sleep_interval)
        
    def reset(self):
        self.finishurls = {}

    @property
    def wait(self):
        return 'wait' == self.cmd
    
    @property
    def stable(self):
        return 'stable' == self.cmd
    
    @property
    def speed(self):
        return 'speed' == self.cmd
    
    @property
    def atry(self):
        times = self.trytimes
        self.trytimes = self.trytimes - 1
        return times > 0
