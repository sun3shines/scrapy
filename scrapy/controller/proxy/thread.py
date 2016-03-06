# -*- coding: utf-8 -*-

import threading
import time
from scrapy.controller.proxy.network import isActive
from scrapy.controller.db.proxyip import seti

class ProxyWorker(threading.Thread):

    def __init__(self,conn,id,host,port):
        threading.Thread.__init__(self) 
        self.conn = conn
        self.id = id
        self.host= host
        self.port = port
 
    def run(self):
        time.sleep(0.1)
        active = 2
        if isActive(self.host, self.port):
            active = 1
        seti(self.conn, [self.id], active)
         
        
    
    
    
