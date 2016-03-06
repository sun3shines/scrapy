# -*- coding: utf-8 -*-

import threading
import time
from scrapy.controller.proxy.network import isActive
from scrapy.controller.db.proxyip import seti

class ProxyWorker(threading.Thread):

    def __init__(self,conn,id,host,port):
        self.conn = conn
        self.id = id
        self.host= host
        self.port = port
        
    def run(self):
        active = 2
        if isActive(self.host, self.port):
            active = 1 
        seti(self.conn, [id], active)
        
        
    
    
    