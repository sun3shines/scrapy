# -*- coding: utf-8 -*-

import json
from scrapy.common.task import Task
from scrapy.controller.route.urls import strUrlMerge,strProxyMerge
import scrapy.common.mission as mission
from scrapy.globalx.static import CONTROLLER_HOST,CONTROLLER_PORT

class LinkMerge(Task):
    
    def __init__(self,urls):
        self.urls = urls
    
    def getUrl(self):
        return strUrlMerge
    
    def getBody(self):
        return json.dumps(self.urls)
    
class ProxyMerge(Task):
    
    def __init__(self,proxys):
        self.proxys = proxys
        
    def getUrl(self):
        return strProxyMerge
    
    def getBody(self):
        return json.dumps(self.proxys)
    
def sendurls(urls):
    t = LinkMerge(urls)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t 

def sendproxys(proxys):
    t = ProxyMerge(proxys)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t 

