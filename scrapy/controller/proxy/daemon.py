# -*- coding: utf-8 -*-

import time
import socket

from scrapy.controller.db.proxyip import puti,geti,seti,rset
from scrapy.controller.db.table.lock.mysql import getdb
from scrapy.controller.proxy.thread import ProxyWorker
from scrapy.controller.db.proxyip import getproxyip
def app_iter(conn):
    attrs = geti(conn, 0)
    print len(attrs)
    for attr in attrs:
        yield (attr['id'],attr['ip'],attr['port'])  
        
def loop():
    
    conn = getdb()
    while True:
        
#        rset(conn)
        time.sleep(1)
        while True:
            print 'again'
            remain = False
            tds = []
            for id,host,port in app_iter(conn):
                remain = True
                tds.append(ProxyWorker(conn,id,host,port))
            for td in tds:
                td.start()
            for td in tds:
                td.join()
            if not remain:
                print 'no more'
                break

        print 'finished'
        time.sleep(60)

if __name__ == '__main__':
    socket.setdefaulttimeout(5)
    loop()

#    conn = getdb()
#    print len(getproxyip(conn,1000))
# daemon的工作，主要进行gets和puts了。并且实在一个循环中处理了。对于gets中的每个端口，开线程，进行修改了。是否需要用锁？因为只有一个进行访问了？
# 获取到id，和完成状态后，由线程，直接对于数据库进行检测了。是的。
# 对于线程的操作，会进行互斥的枷锁了。是的。
