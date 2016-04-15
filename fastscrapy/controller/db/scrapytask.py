# -*- coding: utf-8 -*-

from fastscrapy.controller.db.table.lock.mysql import getlock
from fastscrapy.controller.db.table.scrapytask import insertu,uuid2id

def putu(conn,uuid,starturl):
    # 刚初始化的端口，由后台线程进行验证了。是的。
    with getlock(conn) as mylock:
        if -1 != uuid2id(conn, uuid):
            return
        insertu(conn,uuid,starturl) 
