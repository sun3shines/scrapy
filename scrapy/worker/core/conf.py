# -*- coding: utf-8 -*-

import os
from scrapy.globalx.static import CONTROLLER_HOST,CONTROLLER_PORT, ST_DIR
from scrapy.worker.core.static import PROC_BFS_LIMIT,PROC_DFS_LIMIT,PROC_TOTAL_LIMIT,\
    TRY_TIMES,SLEEP_INTERVAL
    
class Conf:
    def __init__(self,host,parent):

        self.host = host
        self.parent = parent
        
        self.trys = self.gettrytimes()
        self.interval = self.getsleepinterval()
        
        self.pid = os.getpid()
        
        self.bfs = self.getbfs()
        self.dfs = self.getdfs()
        self.total = self.gettotal()

        self.controller_host = self.getcontrollerhost()
        self.controller_port = self.getcontrollerport()
        
    def new(self):
        self.trys = self.gettrytimes()
        
    def decr(self):
        self.trys = self.trys - 1
        
    @property
    def notry(self):
        return  self.trys <= 0
    
    def getbfs(self):
        return PROC_BFS_LIMIT
    
    def getdfs(self):
        return PROC_DFS_LIMIT
    def gettotal(self):
        return PROC_TOTAL_LIMIT
    
    def getcontrollerhost(self):
        return CONTROLLER_HOST
    def getcontrollerport(self):
        return CONTROLLER_PORT
    
    def getlocalhost(self):
        return '192.168.36.201'
    
    def getparent(self):
        return ST_DIR
    
    def gettrytimes(self):
        return TRY_TIMES
    
    def getsleepinterval(self):
        return SLEEP_INTERVAL
    