# -*- coding: utf-8 -*-

import datetime
from scrapy.controller.db.table.link import insertl,fetchl, \
    Link,updatel,resetl,countl,url2id

from scrapy.controller.db.table.lock.mysql import getdb,getlock
  
def puts(conn,urls=[]):
    # 添加之前，需要进行去重了
    with getlock(conn) as mylock:
        for url in urls:
            try:
                if -1 != url2id(conn, url):
                    continue
             
                t = str(datetime.datetime.now())
                insertl(conn, url, t, state=0)
            except:
                pass
        
def gets(conn,limit=0):
    
    attrs = []
    with getlock(conn) as mylock:
        l = Link()
        attrs = fetchl(conn, 0, limit)
        for attr in attrs:
            try:
                id = attr.get(l.id)
                updatel(conn, id, 1)
            except:
                pass
    return attrs

def sets(conn,ids=[],reset=False):
    # merge时会检查，此时重置有意义。
    with getlock(conn) as mylock:
        if ids:
            for id in ids:
                try:
                    updatel(conn, id, 2)
                except:
                    pass
        if reset:
            resetl(conn)
    
def incr(conn):
    if  countl(conn) > 50:
        return True
    return False


if __name__ == '__main__':


    conn = getdb()
    sets(conn,r=True)
    print gets(conn,limit=2)
    conn.close()
