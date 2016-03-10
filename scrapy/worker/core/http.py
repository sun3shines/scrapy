# -*- coding: utf-8 -*-

import json
import os

from scrapy.common.task import Task
from scrapy.controller.route.urls import strUrlPutGet,strHostRemove,strConfigGet
import scrapy.common.mission as mission
from scrapy.globalx.static import CONTROLLER_HOST,CONTROLLER_PORT,PROC_WAIT, \
    PROC_STABLE,PROC_SPEED
    
class Url(Task):
    
    def __init__(self,host,pid,uuid,urls={}):
        
        self.host = host
        self.pid = pid
        self.urls = urls
        self.uuid = uuid
        
    def getUrl(self):
        return strUrlPutGet
    
    def getBody(self):
        return json.dumps(self.urls)
    
    def getHeaders(self):
        return {'host':self.host,
                'pid':self.pid,
                'uuid':self.uuid}
        
    
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
     
class Http:
    
    def __init__(self,http):
        self.http = http
        
    def load(self):
        # 目前来看，配置不需要走任何的网络了。但是留下此参数。可能会有其他的作用了
        pass
    
    def put(self):
        self.http.eliminate()
        t = Url(self.http.host,self.http.pid,self.http.uuid,self.http.input)
        t = mission.execute(self.http.controller_host,self.http.controller_port,t)
        if 2 == t.status/100:
            self.http.cmd = int(t.headers.get('url',0))
            print 'controller cmd ',self.http.cmd
            self.http.output = json.loads(t.data)
            self.http.status = True
        else:
            self.http.new()
            self.http.status = False
        return self.http.status
    
    def delete(self):
        t = HostRmv(self.http.host,self.http.pid)
        mission.execute(self.http.controller_host,self.http.controller_port,t)
    
class senateHttp:
    def __init__(self,c):
        
        self.controller_host = c.controller_host
        self.controller_port = c.controller_port
        self.host = c.host
        self.pid = c.pid
        
        self.uuid = ''
        self.input = []
        
        self.output = []
        self.ecode = 0
        self.cmd = 0
        
    def eliminate(self):
        
        self.cmd = 0
        self.output = []
        self.ecode = 0
        
    def new(self):
        self.input = []
        
    @property
    def status(self):
        return 2 == self.ecode/100
        
    @property
    def wait(self):
        return self.cmd & PROC_WAIT
    
    @property
    def stable(self):
        return self.cmd & PROC_STABLE

    @property
    def speed(self):
        return self.cmd & PROC_SPEED
          
if __name__ == '__main__':
    
    pid = os.getpid()
    host = CONTROLLER_HOST

    t = Url(host,pid)
    t = mission.execute(CONTROLLER_HOST,CONTROLLER_PORT,t)
    
