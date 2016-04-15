# -*- coding: utf-8 -*-

import json
import os

from cloudlib.common.bufferedhttp import jresponse
from cloudlib.common.common.swob import Response
from fastscrapy.globalx.dynamic import conn
from fastscrapy.controller.db.url import puts
from fastscrapy.controller.db.scrapytask import uuid2id
def urlmerge(req):
    
    uuid = req.headers.get('uuid')
    urls = json.loads(req.body)
    uid = uuid2id(conn, uuid)
    puts(conn,urls,uid)           
    # 对于url路径的标准 应在客户端进行，较少服务器的压力
    return Response(status=200)
