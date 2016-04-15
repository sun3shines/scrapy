# -*- coding: utf-8 -*-

from fastscrapy.controller.cache.base import Base
from fastscrapy.controller.cache.port import ports

class hosts(Base):
    
    def __init__(self):
        super(hosts,self).__init__()

    def get(self,host):
        
        h =  self.getd(host)
        if not h:
            h = ports(host)
            self.putd(h.host,h)
        return h
   
HOSTS = hosts()
 
if __name__ == '__main__':
    bx = Base()
    HOSTS = hosts()
