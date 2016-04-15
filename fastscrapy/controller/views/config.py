# -*- coding: utf-8 -*-

import json
import os

from cloudlib.common.bufferedhttp import jresponse
from cloudlib.common.common.swob import Response
from fastscrapy.globalx.static import PROC_TOTAL_LIMIT,PROC_BFS_LIMIT,PROC_DFS_LIMIT, \
    ST_DIR

def get(req):

    headers = {}
    headers.update({'total_limit':PROC_TOTAL_LIMIT})
    headers.update({'bfs_limit':PROC_BFS_LIMIT})
    headers.update({'dfs_limit':PROC_DFS_LIMIT})
    headers.update({'rootdir':ST_DIR})
    
    return Response(status=200,headers = headers)
