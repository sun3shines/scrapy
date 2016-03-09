# -*- coding: utf-8 -*-
import threading

from scrapy.common.requests.task import Url
from scrapy.parse.page import Page

class ParseWorker(threading.Thread):
    def __init__(self,host,port,url,id,classes=[]):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.url = url
        self.id = id
        self.classes = classes
        
    def run(self):
        print self.host,self.port,self.url
        u = Url(self.host,self.port,self.url)
        Page(u.html,u.url,self.classes).parse()
        

def call(http,classes):
 
    s = []
    for t in http.output:   
        pw = ParseWorker(t.get('proxy').get('ip'),t.get('proxy').get('port'),
                         t.get('url'),t.get('id'),classes)
        s.append(pw)
    for pw in s:
        pw.start()
    for t in s:
        pw.join()
        http.input.append(pw.id)
    
# 可以根据host，查找自己定义的position集合了。

