# -*- coding: utf-8 -*-


import json
import os
import sys
import time
import syslog

from scrapy.node.http import sendurls,sendhrmv
from scrapy.node.log import logfork,logexit
from scrapy.node.page import getpage
from scrapy.node.process import Proc

def loop(host,ppath='',ppid=''):

    time.sleep(1)

    current_pid = str(os.getpid())
    logfork(current_pid+' by '+ppid)
    p = Proc(ppath,current_pid)
    
    p.put('dir')
    
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
                        logexit(current_pid)
                        sendhrmv(host, current_pid)
                        p.delele('dir')
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
            if p.count <3:
                syslog.syslog(syslog.LOG_ERR,'childs pid count '+str(p.count))
                newpid = os.fork()
                if 0 == newpid:
                    loop(host,'/'.join([ppath,current_pid]),current_pid)
                else:
                    pass
 
            attrs = json.loads(t.data)
            surls = getpage(attrs)
            continue

        else:
            surls = {}
            continue

if __name__ == '__main__':
   
    import shutil
    shutil.rmtree('/scrapy')
    os.mkdir('/scrapy') 
    loop('192.168.36.201','/scrapy','')
    
