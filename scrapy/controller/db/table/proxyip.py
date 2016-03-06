# -*- coding: utf-8 -*-

class Proxyip(object):
    def __init__(self):
        self.table = 'proxyip'
        self.id = 'id'
        self.ip = 'ip'
        self.port = 'port'
        self.active = 'active'
        
        
def inserti(conn,ip,port,active=0):
    i = Proxyip()
    keys = [i.ip,i.port,i.active]
    vals = [ip,port,active]
    return conn.insert(keys,vals,i.table)

def fetchi(conn,active,limit = 0,rand=True):
    i = Proxyip()
    attrs = []
    
    e = ''
    if rand:
        e = 'WHERE (id >= ((SELECT MAX(id) FROM %s)-(SELECT MIN(id) FROM %s)) * RAND() + (SELECT MIN(id) FROM %s)) AND %s=%s' \
% (i.table,i.table,i.table,i.active,active)
        
    if limit:
        e = e + ' limit '+str(limit)
    
    datas = conn.select(['*'],i.table,{},e)
    if datas:
        for data in datas:
            attr = {}
            attr[i.id] = data[0]
            attr[i.ip] = data[1]
            attr[i.port] = data[2]
            attr[i.active] = data[3]
            attrs.append(attr)
    return attrs


def updatei(conn,active,id=0):
    
    i = Proxyip()
    d = {i.active:active}
    c = {}
    if id:
        c = {i.id:id}
    return conn.update(d,i.table,c)

def proxy2id(conn,host,port):
    i = Proxyip()
    datas = conn.select(['*'],i.table,{i.host:host,i.port:port})
    if datas:
        return datas[0][0]
    return -1
