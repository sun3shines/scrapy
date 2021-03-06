# -*- coding: utf-8 -*-

from cloudcommon.common.bufferedhttp import jresponse
from scrapy.controller.views.url import dispatch
from scrapy.controller.views.host import remove
import scrapy.controller.views.config
from scrapy.center.link import urlmerge
from scrapy.center.proxy import proxymerge

url2view = {}
strUrlPutGet = '/url/dispatch'
url2view.update({strUrlPutGet:dispatch})

strHostRemove = '/host/remove'
url2view.update({strHostRemove:remove})

strConfigGet = '/config/get'
url2view.update({strConfigGet:scrapy.controller.views.config.get})

strUrlMerge = '/url/merge'
url2view.update({strUrlMerge:urlmerge})

strProxyMerge = '/proxy/merge'
url2view.update({strProxyMerge:proxymerge})

def handlerequest(req):
    
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req)

