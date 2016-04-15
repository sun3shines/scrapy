# -*- coding: utf-8 -*-

from fastscrapy.controller.db.proxyip import puti
from fastscrapy.controller.db.table.lock.mysql import getdb
def proxyip():
    
    with file('proxy.txt','r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            host = line.strip().split('=')[1].split(':')[0]
            port = line.strip().split('=')[1].split(':')[1]
            yield (host,port)
                
def initdb():
    conn = getdb()
    for host,port in proxyip():
        puti(conn, [(host,port)],active=0)
        
if __name__ == '__main__':
    initdb()
    
