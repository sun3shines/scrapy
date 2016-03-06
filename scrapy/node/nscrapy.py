# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil

from scrapy.node.proc import Proc
from scrapy.node.fs import initlock
from scrapy.globalx.static import ROOT_DIR

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
    p = None
    for p in get_response(host, parent,p):
        if p.wait:
            p.sleep()
            if p.root !=p.parent:
                if p.atry:
                    p.reset()
                else:
                    if not p.empty:
                        p.reset()
                    else:
                        p.destroy()
            else:
                p.reset()
        elif p.stable:
            p.run()
        elif p.speed:
            if p.allow:
                if 0 == p.fork():
                    main(p.host,p.path)
                    sys.exit(0)
            p.run()

if __name__ == '__main__':
   
    shutil.rmtree(ROOT_DIR)
    os.mkdir(ROOT_DIR) 
    initlock('/'.join([ROOT_DIR,'lock']))
    main('192.168.36.201',ROOT_DIR)
    