# -*- coding: utf-8 -*-

class Scrapy(object):
    def __init__(self):
        self.table = 'scrapy'
        self.id = 'id'
        self.uuid = 'uuid'
        self.starturl = 'starturl'
    
def insertu(conn,uuid,starturl):
    s = Scrapy()
    keys = [s.uuid,s.starturl]
    vals = [uuid,starturl]
    return conn.insert(keys,vals,s.table)

def uuid2id(conn,uuid):
    s = Scrapy()
    datas = conn.select(['*'],s.table,{s.uuid:uuid})
    if datas:
        return datas[0][0]
    return -1
