# -*- coding: utf-8 -*-


import json
import os
import sys
import time
import syslog
import shutil

from scrapy.node.http import sendurls,sendhrmv,recvconf
from scrapy.node.log import logfork,logexit,logerror
from scrapy.node.page import getpage
from scrapy.node.proc import Proc
from scrapy.node.fs import listattrs,initlock,incrlock,decrlock

def get_response(host,parent,p=None):
    
    if not p:
        p = Proc(host,parent)
        p.create()
    
    while True:
        if not p.send():
            continue
        yield p
    
def main(host,parent):
   
    time.sleep(1)
    # 关键是在这里，从子进程，切换会父进程了 
    available = True
    p = None
    for p in get_response(host, parent,p):
        if p.wait:
            p.sleep()
            if p.root !=p.parent:
                if available:
                    available = False
                    p.reset()
                else:
                    if not p.empty:
                        p.reset()
                    else:
                        p.destroy()
            else:
                p.reset()
        elif p.stable:
            available =  True
            p.run()
        elif p.speed:
            available =  True
            if p.allow:
                if 0 == p.fork():
                    main(p.host,p.path)
                    sys.exit(0)
            p.run()

if __name__ == '__main__':
   
    shutil.rmtree('/scrapy')
    os.mkdir('/scrapy') 
    initlock('/scrapy/lock')
    main('192.168.36.201','/scrapy')
    
