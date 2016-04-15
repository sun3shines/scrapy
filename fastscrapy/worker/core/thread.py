# -*- coding: utf-8 -*-
import threading

from fastscrapy.common.requests.task import Url
from fastscrapy.parse.page import Page

class ParseWorker(threading.Thread):
    def __init__(self,host,port,url,id,uuid,classes):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.url = url
        self.id = id
        self.classes = classes
        self.uuid = uuid

    def run(self):
        print self.host,self.port,self.url
        u = Url(self.host,self.port,self.url)
        Page(u.html,u.url,self.uuid,self.classes).parse()
        

def call(http,classes):
 
    s = []
    for t in http.output:   
        pw = ParseWorker(t.get('proxy').get('ip'),t.get('proxy').get('port'),
                         t.get('url'),t.get('id'),http.uuid,classes)
        s.append(pw)
    for pw in s:
        pw.start()
    http.input = []
    for t in s:
        pw.join()
        http.input.append(pw.id)
    
# 可以根据host，查找自己定义的position集合了。

