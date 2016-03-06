# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from scrapy.controller.cache.node import nodeinc,nodeput,nodermv

def remove(req):
    
    param = req.headers
    host = param.get('host')
    pid = param.get('pid')
    nodermv(host, pid)
    return Response(status=200)