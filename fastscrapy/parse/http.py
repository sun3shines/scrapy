# -*- coding: utf-8 -*-

import json
from fastscrapy.common.task import Task
from fastscrapy.controller.route.urls import strUrlMerge,strProxyMerge
import fastscrapy.common.mission as mission
from fastscrapy.globalx.static import CONTROLLER_HOST,CONTROLLER_PORT

class LinkMerge(Task):
    
    def __init__(self,urls,uuid):
        self.urls = urls
        self.uuid = uuid
        
    def getUrl(self):
        return strUrlMerge
    
    def getBody(self):
        return json.dumps(self.urls)
    
    def getHeaders(self):
        return {'uuid':self.uuid}
    
class ProxyMerge(Task):
    
    def __init__(self,proxys):
        self.proxys = proxys
        
    def getUrl(self):
        return strProxyMerge
    
    def getBody(self):
        return json.dumps(self.proxys)
    
def sendurls(urls,uuid):
    t = LinkMerge(urls,uuid)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t 

def sendproxys(proxys):
    t = ProxyMerge(proxys)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    return t 

