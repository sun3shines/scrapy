# -*- coding: utf-8 -*-

import datetime
import time

from scrapy.globalx.static import URL_RESET_PERIOD
class Link:
    def __init__(self):
        self.table = 'link'
        self.id = 'id'
        self.url = 'url'
        self.time = 'time'
        self.state = 'state'
        
        # type 0: in ,1:out 2:finished
        
def insertl(conn,url,time,state=0):
    l = Link()
    keys = [l.url,l.time,l.state]
    vals = [url,time,state]
    
    return conn.insert(keys,vals,l.table)


def updatel(conn,id,state,time=''):
    
    l = Link()
    d = {l.state:state}
    if time:
        d.update({l.time:time})
    return conn.update(d,l.table,{l.id:id})

def resetl(conn):

    # 解决好时间问题。    
    l = Link()
    d = {l.state:0}
    t = str(datetime.datetime.now())
    d.update({l.time:t})
    now = time.time()
    e = 'where state = 1 and %s-UNIX_TIMESTAMP(time) > %s' % (str(now),URL_RESET_PERIOD)
    return conn.update(d,l.table,{},e)

def fetchl(conn,state,limit=0):
    
    l = Link()
    attrs = []
    if limit:
        e = ' limit '+str(limit)
    else:
        e = ''
    datas = conn.select(['*'],l.table,{l.state:state},e)
    if datas:
        for data in datas:
            attr = {}
            attr[l.id] = data[0]
            attr[l.url] = data[1]
#            attr[l.time] = data[2]
            attr[l.state] = data[3]
            attrs.append(attr)
    return attrs

def countl(conn):
    
    l = Link()
    datas = conn.select(['count(%s)' % (l.url)],l.table,{l.state:0})
    return datas[0][0]

def url2id(conn,url):
    
    l = Link()
    datas = conn.select(['*'],l.table,{l.url:url})
    if datas:
        return datas[0][0]
    return -1

