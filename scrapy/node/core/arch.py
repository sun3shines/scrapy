# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil

from scrapy.node.core.proc import Proc
from scrapy.node.core.fs import initlock
from scrapy.globalx.static import ROOT_DIR
from scrapy.globalx.static import CONTROLLER_HOST

def get_response(host,parent,p=None):
    
    if not p:
        p = Proc(host,parent)
        p.create()
    
    while True:
        if not p.send():
            continue
        yield p
    
def main(host,parent):

    time.sleep(0.5)
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


def start():   
    shutil.rmtree(ROOT_DIR)
    os.mkdir(ROOT_DIR) 
    initlock('/'.join([ROOT_DIR,'lock']))
    main(CONTROLLER_HOST,ROOT_DIR)
   
 
