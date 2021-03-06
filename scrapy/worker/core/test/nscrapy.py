# -*- coding: utf-8 -*-


import json
import os
import sys
import time
import syslog
import shutil

from scrapy.worker.http import sendurls,sendhrmv,recvconf
from scrapy.worker.log import logfork,logexit,logerror
from scrapy.worker.page import getpage
from scrapy.worker.process import Proc
from scrapy.worker.fs import listattrs,initlock,incrlock,decrlock
from scrapy.globalx.static import CONTROLLER_HOST

def loop(host,ppath='',ppid=''):

    time.sleep(1)
    
    current_pid = str(os.getpid())
    t = recvconf()
    if 2 != t.status/100:
        logerror(current_pid, 'recv controller config failed .exit.')
        sys.exit(0)
        
    
    # logfork(current_pid+' by '+ppid)
    p = Proc(ppath,current_pid)
    p.put('dir')
    p.total = int(t.headers.get('total_limit',0))
    p.dfs = int(t.headers.get('dfs_limit',0))
    p.bfs = int(t.headers.get('bfs_limit',0))
 
    surls = {}
    available = True
    
    while True:
        t = sendurls(host, current_pid, surls)
        if 2 != t.status/100:
            surls = {}
            continue
        
        param = t.headers
        cmd = param.get('url')
        print cmd        
        if 'wait' == cmd:
            time.sleep(5)
            
            if '/scrapy' !=ppath:
                if available:
                    available = False
                    surls = {}
                    continue
                
                else:
                    if not p.empty:
                        surls = {}
                        continue
                    else:
                        # logexit(current_pid)
                        sendhrmv(host, current_pid)
                        p.delele('dir')
                        decrlock(p.lockpath,p.total)
                        sys.exit(0)
            else:
                surls = {}
                continue
            
        elif 'stable' == cmd:
            
            available =  True
            attrs = json.loads(t.data) 
            surls = getpage(attrs)
            continue
        
        elif 'speed' == cmd:
            
            available =  True
            if p.count <int(p.bfs) and incrlock(p.lockpath, p.total):
                newpid = os.fork()
                if 0 == newpid:
                    loop(host,'/'.join([ppath,current_pid]),current_pid)
                    sys.exit(0) 

            attrs = json.loads(t.data)
            surls = getpage(attrs)
            continue

        else:
            surls = {}
            continue

if __name__ == '__main__':
   
    shutil.rmtree('/scrapy')
    os.mkdir('/scrapy') 
    initlock('/scrapy/lock')
    loop(CONTROLLER_HOST,'/scrapy','')
    
