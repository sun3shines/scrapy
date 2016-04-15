# -*- coding: utf-8 -*-

import datetime
from fastscrapy.controller.db.table.proxyip import Proxyip,inserti,\
    updatei,fetchi,proxy2id

from fastscrapy.controller.db.table.lock.mysql import getdb,getlock

def puti(conn,proxys,active=0):
    # 刚初始化的端口，由后台线程进行验证了。是的。
    with getlock(conn) as mylock:
        for host,port in proxys:
            try:
                if -1 != proxy2id(conn, host, port):
                    continue
                inserti(conn, host, port, active=0)
            except:
                pass

def geti(conn,active,limit=200,rand=True):
    # active 为0 为后台线程使用
    # active 为1 为scrapy线程使用
    i = Proxyip()
    
    with getlock(conn) as mylock:
        attrs = fetchi(conn, active, limit, rand)
        if 0 != active:
            return attrs
        # 防止被重复抓取，too many sockets 
        for attr in attrs:
            try:
                id = attr.get(i.id)
                updatei(conn, 3, id)
            except:
                pass
        return attrs

def seti(conn,ids,active):
    # active 为1，2 为后台线程使用， updatei只有后台进程来使用了。
    with getlock(conn) as mylock:
        for id in ids:
            try:
                updatei(conn, active, id)
            except:
                pass
    
def rset(conn):
    with getlock(conn) as mylock:
        updatei(conn, 0, id=0)
    
# 关于proxyip的种种操作。

# 随机选取 选取状态为1的。

# 后台重置

# 后台随机选取（选取刚初始化的），后台测试，后台更新。 选取100个，然后采用线程对其进行更新了？使用线程吧。是的。

# 插入？只有一个插入，批量插入，没有太多的选择了。

# 后台线程，会判断数量了。如果抓取的数量为0，则后台线程停止20分钟了。是的。

# 如果没有代理IP，则强制wait了，不执行任务。是的。必须要有代理ip了。

def getproxyip(conn,limit):

    ips = []
    i = Proxyip()
    while len(ips) < limit:
        print 'again'
        attrs = fetchi(conn, 1, limit)
        ips.extend(attrs)
    return ips

if __name__ == '__main__':
    conn = getdb()
    print len(getproxyip(conn,200))
