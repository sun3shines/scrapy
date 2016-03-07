# -*- coding: utf-8 -*-

import socket
from scrapy.common.requests.task import Url

def isActive(host,port):
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((host,int(port)))
        sock.shutdown(2) 
        sock.close() 
        return True
    except:
        sock.close()
        return False

def htmlActive(host,port):
    try:
        u = Url(host,port,'http://www.haodailiip.com/guoji/1',True)
        if 2 != int(u.status/100):
            return False
        return True
    except:
        print 'html active error ',host,port
        return False

