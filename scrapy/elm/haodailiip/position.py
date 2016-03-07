# -*- coding: utf-8 -*-

from scrapy.utils.path import urlpath
from scrapy.elm.http import sendproxys,sendurls
import time

class Link:
    def __init__(self,html):
        self.html = html
        self.urls = []
 
    def parse(self):
        time.sleep(5)
        try: 
            hrefs = self.html.find('td',{'class':'td760'}).findAll('a')
            self.urls = [urlpath('/'.join(['www.haodailiip.com',a.get('href')])) for a in hrefs]
        except:
            print 'ERROR\n\n\n'
            print self.html,'\n\n\n'

        self.push()
        time.sleep(5)

    def push(self):
        sendurls(self.urls) 

class Content:
    
    def __init__(self,html):
        self.html = html
        
    def parse(self):
#        time.sleep(5)
#        try:
#            table = self.html.find('',{'class':'proxy_table'})
        pass
    
    def push(self):
        pass
