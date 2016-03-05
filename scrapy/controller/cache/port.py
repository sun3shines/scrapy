# -*- coding: utf-8 -*-

from scrapy.controller.cache.base import Base
from scrapy.globalx.static import PROC_TOTAL_LIMIT
import syslog

class ports(Base):
    def __init__(self,host):
        super(ports,self).__init__()
        self.host = host

    def put(self,port):
        self.putl(port)
        
    def rmv(self,port):
        self.rmvl(port)
 
    @property
    def inc(self):
        count = self.countl
        return int(count) < int(PROC_TOTAL_LIMIT)
