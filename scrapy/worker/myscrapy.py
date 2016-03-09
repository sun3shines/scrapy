# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.worker.core.arch import Scrapy
from scrapy.worker.core.proc import Proc
from scrapy.globalx.static import ST_DIR

class MyProc(Proc):
    
    def getclasses(self):
        return []
    
class MySracpy(Scrapy):
    
    def getproc(self):
        return MyProc
        
if __name__ == '__main__':
    
    LOCAL_HOST = '192.168.36.201'
    MySracpy('proxyhaodaili','www.haodailiip.com/guonei/1').start(LOCAL_HOST, ST_DIR)
    

