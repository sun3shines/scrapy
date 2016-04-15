# -*- coding: utf-8 -*-

import json
import os

from cloudlib.common.bufferedhttp import jresponse
from cloudlib.common.common.swob import Response
from fastscrapy.controller.cache.node import nodeinc,nodeput,nodermv

def remove(req):
    
    param = req.headers
    host = param.get('host')
    pid = param.get('pid')
    nodermv(host, pid)
    print 'remove proc: ',host,pid
    return Response(status=200)
