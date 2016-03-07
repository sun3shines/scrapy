# -*- coding: utf-8 -*-
import threading

from scrapy.common.requests.task import Url
from scrapy.elm.page import Page

class ParseWorker(threading.Thread):
    def __init__(self,host,port,url,id):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.url = url
        self.id = id
        
    def run(self):
        print self.host,self.port,self.url
        u = Url(self.host,self.port,self.url)
        Page(u.html).parse()
        

def call(tasks):
 
    finishurls = []
    s = []
    for t in tasks:   
        pw = ParseWorker(t.get('proxy').get('ip'),t.get('proxy').get('port'),
                         t.get('url'),t.get('id'))
        s.append(pw)
    for pw in s:
        pw.start()
    for t in s:
        pw.join()
        finishurls.append(pw.id)
    return finishurls
     
# 可以根据host，查找自己定义的position集合了。
    
