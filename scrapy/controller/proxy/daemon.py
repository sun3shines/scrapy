# -*- coding: utf-8 -*-

import time
import socket

from scrapy.controller.db.proxyip import puti,geti,seti,rset
from scrapy.controller.db.table.lock.mysql import getdb
from scrapy.controller.proxy.thread import ProxyWorker

def app_iter(conn):
    attrs = geti(conn, 0)
    for attr in attrs:
        yield (attr['id'],attr['ip'],attr['port'])  
        
def loop():
    
    conn = getdb()
    while True:
        
        rset(conn)
        time.sleep(1)
        while True:
            print 'again'
            remain = False
            for id,host,port in app_iter(conn):
                remain = True
                ProxyWorker(conn,id,host,port).start()
            if not remain:
                print 'no more'
                break

        print 'finished'
        time.sleep(60*20)

if __name__ == '__main__':
    socket.setdefaulttimeout(5)
    loop()

# daemon的工作，主要进行gets和puts了。并且实在一个循环中处理了。对于gets中的每个端口，开线程，进行修改了。是否需要用锁？因为只有一个进行访问了？
# 获取到id，和完成状态后，由线程，直接对于数据库进行检测了。是的。
# 对于线程的操作，会进行互斥的枷锁了。是的。
