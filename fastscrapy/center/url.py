# -*- coding: utf-8 -*-

import threading
from fastscrapy.controller.db.url import puts
from fastscrapy.controller.db.table.lock.mysql import getdb
from fastscrapy.utils.path import urlpath
import time

class Worker(threading.Thread):

    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        while True:
            url = 'www.haodailiip.com/guoji/1' 
            url = urlpath(url)
            
            puts(self.conn,[url])            
            time.sleep(1)
            break

if __name__ == '__main__':

#    Worker(db).start()
#    while True:
#        time.sleep(5)
#    site = 'www.xicidaili.com/nn/1'
    site = 'www.haodailiip.com/guonei/1'
    url = urlpath(site)
    db = getdb()
    puts(db,[url])
    db.close()
    
