# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from scrapy.controller.db.url import gets,incr,sets,puts
from scrapy.globalx.dynamic import conn
from scrapy.controller.cache.node import nodeinc,nodeput,nodermv
from scrapy.node.log import logurls 

def merge(ids):
    
    pass

def dispatch(req):
    # 会在客户端进行url的标准化，减少服务端的压力
    param = req.headers    
    urls = json.loads(req.body)
    host = param.get('host')
    pid = param.get('pid')
    nodeput(host, pid)
    newURLs = []
    ids = []
    for id in urls:
        ids.append(id)
        newURLs.extend(urls[id])
       
    logurls(pid,ids) 

    sets(conn,ids,r=True)
    puts(conn,newURLs)
    
    attrs = gets(conn,1)
    attrs = json.dumps(attrs)
 
    # incr(conn)
    headers = {}
    if not attrs:
        headers = {'url':'wait'}
    else:
        if nodeinc(host):
            headers = {'url':'speed'}
        else:
            headers = {'url':'stable'}
        
    return Response(body=attrs,status=200,headers=headers)

def remove(req):
    
    param = req.headers
    host = param.get('host')
    pid = param.get('pid')
    nodermv(host, pid)
    return Response(status=200)

