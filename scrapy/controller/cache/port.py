# -*- coding: utf-8 -*-

from scrapy.controller.cache.base import Base
from scrapy.globalx.static import NODE_NUM_LIMIT
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
        syslog.syslog(syslog.LOG_ERR,'host pid count '+str(count))
        print int(count), int(NODE_NUM_LIMIT)
        return int(count) < int(NODE_NUM_LIMIT)
#        return 18 < 10
