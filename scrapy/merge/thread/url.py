# -*- coding: utf-8 -*-

import threading
from scrapy.controller.db.url import puts
from scrapy.controller.db.table.lock.mysql import getdb
from scrapy.utils.path import urlpath
import time

class Worker(threading.Thread):

    def __init__(self,conn):
        self.conn = conn

    def run(self):
        while True:
            url = str(time.time())
            
            url = urlpath(url)
            
            puts(self.conn,[url])            
            time.sleep(1)


if __name__ == '__main__':

    db = getdb()
    Worker(db).start()
    while True:
        time.sleep(5)
    
