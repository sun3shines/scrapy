# -*- coding: utf-8 -*-

from cloudcommon.common.bufferedhttp import jresponse
from scrapy.controller.views.url import dispatch,remove

url2view = {}
strUrlPutGet = '/url/put/get'
url2view.update({strUrlPutGet:dispatch})

strHostRemove = '/host/remove'
url2view.update({strHostRemove:remove})

def handlerequest(req):
    
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req)

