# -*- coding: utf-8 -*-

import os
import sys
import time

from scrapy.worker.core.proc import Proc
from scrapy.globalx.static import ST_DIR

class Scrapy:
    
    def __init__(self,uuid,starturl):
        self.uuid = uuid
        self.starturl = starturl
    
    def get_response(self,host,parent,p=None):
        
        if not p:
            p = self.getproc()(host,parent)
            p.create()
            p.start(self.uuid,self.starturl)
        while True:
            if not p.send():
                p.sleep()
                continue
            yield p
        
    def start(self,host,parent):
        print 'parent: ',parent
        time.sleep(0.5)
        # 关键是在这里，从子进程，切换会父进程了 
        p = None
        for p in self.get_response(host, parent,p):
            if p.wait :
                p.sleep()
                if p.posterity and p.notry and p.empty:
                    p.destroy()
            
            elif p.speed:
                if p.allow:
                    if 0 == p.fork():
                        self.start(p.c.host,p.st.path)
                        sys.exit(0)
            p.run()
    
    def getproc(self):
        return Proc
    
if __name__ == '__main__':
    
    LOCAL_HOST = '127.0.0.1'
    Scrapy.start(LOCAL_HOST,ST_DIR)
   
 
