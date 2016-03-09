# -*- coding: utf-8 -*-

import os
import time
import sys

from scrapy.worker.core.http import Http,senateHttp
from scrapy.worker.core.thread import call
from scrapy.worker.core.fst import FSt,senateFSt
from scrapy.worker.core.conf import Conf
from scrapy.controller.db.url import puts
from scrapy.controller.db.scrapy import putu,uuid2id
from scrapy.controller.db.table.lock.mysql import getdb
from scrapy.utils.path import urlpath

class Proc:
    
    def __init__(self,host,parent):
        
        self.c = self.getconf()(host,parent)
        self.st = senateFSt(self.c)
        self.http = senateHttp(self.c)
        
    @property
    def empty(self):
        return FSt(self.st).empty()

    @property
    def count(self):   
        FSt(self.st).count

    @property
    def bfs(self):
        return self.c.bfs
    
    @property
    def dfs(self):
        return self.c.dfs
    
    @property
    def total(self):
        return self.c.total
       
    @property
    def level(self):
        return FSt(self.st).level
    
    @property
    def incr(self):
        return FSt.incr(self.st)
    
    @property
    def allow(self):
        return ( self.count <self.bfs and self.level < self.dfs 
                 and self.incr)
        
    @property
    def wait(self):
        return self.http.wait
    
    @property
    def stable(self):
        return self.http.stable
    
    @property
    def speed(self):
        return self.http.speed
            
    @property
    def notry(self):
        return self.c.notry
    @property
    def posterity(self):
        return not self.st.ancestor
    
    def getclasses(self):
        return []
    
    def getconf(self):
        return Conf
    
    def fork(self):
        return os.fork()
         
    def create(self):
        Http(self.http).load()
        self.st.load()
        FSt(self.st).put()
        
    def destroy(self):
                
        Http(self.http).delete()
        FSt(self.st).delete()
        FSt(self.st).decr()
        sys.exit(0)
    
    def sleep(self):
        if self.wait:
            self.c.decr()
        time.sleep(self.c.interval)

    def send(self):
        return Http(self.http).put()
    
    def run(self):
        if self.wait:
            self.http.new()
        else:
            self.c.new()
            call(self.http,self.getclasses())
            
    def start(self,starturl,scrapyuuid):
        
        try:
            db = getdb()
            starturl = urlpath(starturl)
            putu(db,scrapyuuid,starturl)
            uid = uuid2id(db, scrapyuuid)
            puts(db,[starturl],uid)
        finally:
            db.close()
    