# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from scrapy.globalx.dynamic import conn
from scrapy.controller.db.proxyip import puti

def proxymerge(req):
    
    attrs = json.loads(req.body)
    proxys = []
    for attr in attrs:
        proxys.append((attr.get('ip'),attr.get('port')))
    puti(conn,proxys,active=0)           
    # 对于url路径的标准 应在客户端进行，较少服务器的压力
    return Response(status=200)
