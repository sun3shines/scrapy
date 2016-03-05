# -*- coding: utf-8 -*-

import json
import os

from scrapy.common.task import Task
from scrapy.controller.route.urls import strUrlPutGet,strHostRemove,strConfigGet
import scrapy.common.mission as mission
from scrapy.globalx.static import CONTROLLER_HOST,CONTROLLER_PORT
class Url(Task):
    
    def __init__(self,host,pid,urls={}):
        
        self.host = host
        self.pid = pid
        self.urls = urls
    
    def getUrl(self):
        return strUrlPutGet
    
    def getBody(self):
        return json.dumps(self.urls)
    
    def getHeaders(self):
        return {'host':self.host,
                'pid':self.pid}
        
    
class HostRmv(Task):
    
    def __init__(self,host,pid):
        self.host = host
        self.pid = pid
        
    def getHeaders(self):
        return {'host':self.host,
                'pid':self.pid}
        
    def getUrl(self):
        return strHostRemove

class ConfGet(Task):
    def __init__(self):
        pass
    def getHeaders(self):
        return {}
    
    def getUrl(self):
        return strConfigGet
    
def sendurls(host,pid,urls):
    t = Url(host,pid,urls)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t 

def sendhrmv(host,pid):
    t = HostRmv(host,pid)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t

def recvconf():
    t = ConfGet()
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t     
   
if __name__ == '__main__':
    pid = os.getpid()
    host = CONTROLLER_HOST

    t = Url(host,pid)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    
