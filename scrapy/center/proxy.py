# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from scrapy.globalx.dynamic import conn
from scrapy.controller.db.proxyip import puti

def proxymerge(req):
    
    proxys = json.loads(req.body)
    puti(conn,proxys,active=0)           
    # 对于url路径的标准 应在客户端进行，较少服务器的压力
    return Response(status=200)
