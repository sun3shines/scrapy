# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from BeautifulSoup import BeautifulSoup
from scrapy.elm.haodailiip.position import Link,Content
import scrapy.elm.xicidaoli.position

class Page(object):
    def __init__(self,html,url):
        self.f = BeautifulSoup(html)
        self.site = url.split('/')[0]

        # 主要是作为针对每个网站的各种的路由了。因为不清楚获取到的是那个site的url了
        try:
            file('/usr/lib/python2.6/site-packages/scrapy/elm/html.txt','w').write(html)
        except:
            pass

    def getpostions(self):
        if 'www.haodailiip.com' == self.site:
            return [Link,Content]
        elif 'www.xicidaili.com' == self.site:
            return [scrapy.elm.xicidaoli.position.Link,scrapy.elm.xicidaoli.position.Content]

    def parse(self):
        for position_class in self.getpostions():
            position_class(self.f).parse()
   
if __name__ == '__main__':

    page = Page(file('html.txt').read(),'www.xicidaili.com') 
    page.parse()

