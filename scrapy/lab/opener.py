# -*- coding: utf-8 -*-
import urllib2
from gzip import GzipFile
from StringIO import StringIO
import zlib

def ProxyHandler(proxystr):
    proxy_support = urllib2.ProxyHandler({'http':proxystr}) 
    return proxy_support

def mixUrllib2(pstr):
    handlers = []

    handlers.append(ProxyHandler(pstr)) 
    handlers.append(EncodingOpener)
    handlers.append(urllib2.HTTPHandler)

    opener = urllib2.build_opener(*handlers)  
    urllib2.install_opener(opener)  
    return urllib2

class EncodingOpener(urllib2.BaseHandler):

    def http_request(self,req):
        req.add_header('Accept-Encoding','gzip, deflate')
        return req
    
    def http_response(self,req,resp):
        old_resp = resp
        if 'gzip' == resp.headers.get('content-encoding'):
            gz = GzipFile(fileobj=StringIO(resp.read()),mode='r')
            resp = urllib2.addinfourl(gz,old_resp.headers,old_resp.url,old_resp.code)
            resp.msg = old_resp.msg

        if 'deflate' == resp.headers.get('content-encoding'):
            gz = StringIO(deflate(resp.read()))
            resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code) 
            resp.msg = old_resp.msg
        return resp 

def deflate(data):
    try:
        return zlib.decompress(data,-zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

def KeepAliveOpener():

    # import urllib2
    # from urlgrabber.keepalive import HTTPHandler as keepAliveHandler
    # keepalive_handler = HTTPHandler()
    # opener = urllib2.build_opener(keepalive_handler)
    # urllib2.install_opener(opener)
    # python-urlgrabber-3.9.1-9.el6.noarch
    # http://stackoverflow.com/questions/1037406/python-urllib2-with-keep-alive
    pass
# 可以builder多个opener
# build_opener列表了。是的。
