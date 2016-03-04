# -*- coding: utf-8 -*-

class Link:
    def __init__(self):
        self.table = 'link'
        self.id = 'id'
        self.url = 'url'
        self.time = 'time'
        self.state = 'state'
        
        # type 0: in ,1:out 2:finished
        
def insert_linkobj(conn,url,time,state=0):
    l = Link()
    keys = [l.url,l.time,l.state]
    vals = [url,time,state]
    
    return conn.insert(keys,vals,l.table)


def udpate_linkobj(conn,id,state):
    
    l = Link()
    d = {l.state:state}
    return conn.update(d,l.table,{l.id:id})

def reset_linkobj(conn):

    # 解决好时间问题。    
    l = Link()
    d = {l.state:0}
    return conn.update(d,l.table,{},'where state = 1 and UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(time) > 60')

def s2attrs(conn,state,limit=True):
    
    l = Link()
    attrs = []
    if limit:
        e = ' limit 1'
    else:
        e = ''
    datas = conn.select(['*'],l.table,{l.state:state},e)
    if datas:
        for data in datas:
            attr = {}
            attr[l.id] = data[0]
            attr[l.url] = data[1]
            attr[l.time] = data[2]
            attr[l.state] = data[3]
            attrs.append(attr)
    return attrs
