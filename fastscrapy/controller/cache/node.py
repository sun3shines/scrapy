# -*- coding: utf-8 -*-

from fastscrapy.globalx.dynamic import HOSTS

def nodeput(host,port):
    
    HOSTS.get(host).put(port)
    
def nodermv(host,port):
    
    HOSTS.get(host).rmv(port)

def nodeinc(host):
    return HOSTS.get(host).inc

if __name__ == '__main__':

    nodeput('127.0.0.1','9001')
    nodeput('127.0.0.1','9002')

    nodeput('127.0.0.2','9001')
    nodeput('127.0.0.2','9002')
    

