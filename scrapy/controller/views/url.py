# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from scrapy.controller.db.url import gets,incr,sets,puts
from scrapy.globalx.dynamic import conn
from scrapy.controller.cache.node import nodeinc,nodeput,nodermv
from scrapy.node.core.log import logurls 
from scrapy.controller.db.proxyip import getproxyip
from scrapy.globalx.static import URLS_LIMIT
from scrapy.controller.views.format import filter,printattrs

def dispatch(req):
    
    # 会在客户端进行url的标准化，减少服务端的压力
    param = req.headers    
    finishids = json.loads(req.body)
    host = param.get('host')
    pid = param.get('pid')
    nodeput(host, pid)
    
    sets(conn,finishids,reset=False)
    attrs = gets(conn,limit=URLS_LIMIT)
    
    headers = {}
    if not attrs:
        headers = {'url':'wait'}
    else:
        proxys = getproxyip(conn, limit=len(attrs))
        inti = 0
        while inti < len(attrs):
            attrs[inti].update({'proxy':proxys[inti]})
            inti = inti + 1
    
        if nodeinc(host):
            headers = {'url':'speed'}
        else:
            headers = {'url':'stable'}
    printattrs(pid,attrs)
    attrs = json.dumps(filter(attrs))
    return Response(body=attrs,status=200,headers=headers)

