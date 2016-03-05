# -*- coding: utf-8 -*-

import json
import os

from scrapy.common.task import Task
from scrapy.controller.route.urls import strUrlPutGet,strHostRemove
import scrapy.common.mission as mission

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

def sendurls(host,pid,urls):
    t = Url(host,pid,urls)
    t = mission.execute('127.0.0.1',7020,t)
    return t 

def sendhrmv(host,pid):
    t = HostRmv(host,pid)
    t = mission.execute('127.0.0.1',7020,t)
    return t 
    
if __name__ == '__main__':
    pid = os.getpid()
    host = '127.0.0.1'

    t = Url(host,pid)
    t = mission.execute('127.0.0.1',7020,t)
    
