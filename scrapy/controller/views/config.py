# -*- coding: utf-8 -*-

import json
import os

from cloudcommon.common.bufferedhttp import jresponse
from cloudcommon.common.common.swob import Response
from scrapy.globalx.static import PROC_TOTAL_LIMIT,PROC_BFS_LIMIT,PROC_DFS_LIMIT

def get(req):
    
    headers = {}
    headers.update({'total_limit':PROC_TOTAL_LIMIT})
    headers.update({'bfs_limit':PROC_BFS_LIMIT})
    headers.update({'dfs_limit':PROC_DFS_LIMIT})
    return Response(status=200,headers = headers)