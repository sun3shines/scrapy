# -*- coding: utf-8 -*-

from scrapy.utils.path import urlpath
from scrapy.elm.http import sendproxys,sendurls
import time

class Link:
    def __init__(self,html):
        self.html = html
        self.urls = []
 
    def parse(self):
        try: 
            hrefs = self.html.find('td',{'class':'td760'}).findAll('a')
            self.urls = [urlpath('/'.join(['www.haodailiip.com',a.get('href')])) for a in hrefs]
        except:
            print 'ERROR\n\n\n'
            print self.html,'\n\n\n'

        self.push()

    def push(self):
        sendurls(self.urls) 

class Content:
    
    def __init__(self,html):
        self.html = html
        self.attrs = []        
    def parse(self):

        # IP  端口  类型  匿名度
        # 110.136.226.196  8080  HTTP  高匿
        try:
            table = self.html.find('table',{'class':'proxy_table'})
            trs = table.findAll('tr')
            for tr in trs:
                tds = tr.findAll('td')
                attr = {}
                attr['ip'] = tds[0].text.strip()
                if attr['ip'].startswith('IP'):
                    continue

                attr['port'] = tds[1].text.strip()
                attr['scheme'] = tds[3].text.strip()
                attr['anonymous'] = tds[4].text.strip()
                self.attrs.append(attr)

            self.push()
        except: 
            pass
            
    def push(self):
        sendproxys(self.attrs) 
