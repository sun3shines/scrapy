# -*- coding:utf8 -*-

import requests
import re
import time
from BeautifulSoup import BeautifulSoup
import socket

class Host(object):

    def __init__(self):
        self.rootdir = ''
        self.startUrl = ''
        self.prefix = ''

        self.datadir = ''
        self.headers = {}
        self.queuehrefs = []
        self.userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'
       
    @property
    def dirName(self):
        return self.prefix.replace('http://','').split('/')[0].replace('.','')

    def getHeaders(self):
        return {'User-Agent':self.userAgent}


    def nextpage(self,bsObj):
        return ''

    def getpage(self,url):
        resp = requests.get(url,headers=self.getHeaders())
        html = resp.text
        bsObj = BeautifulSoup(html)
        return bsObj

    def genNextPageLinks(self):

        self.queuehrefs = []
        self.queuehrefs.append(self.startUrl)
        while len(self.queuehrefs) > 0:
            url = self.queuehrefs.pop(0)
            print url

            page = self.getpage(url)
            nextpagelink = self.nextpage(page)

            if nextpagelink in self.queuehrefs:
                continue

            self.queuehrefs.append(self.prefix+nextpagelink)

            time.sleep(1)

class MyHost(Host):

    def __init__(self):
        super(MyHost,self).__init__()
        self.rootdir = '/root/scrapy/utils'
        self.startUrl = 'http://www.xicidaili.com/wn/'
        self.prefix = 'http://www.xicidaili.com'

        self.datadir = self.rootdir + '/' + 'anonymous' + '/' + self.dirName 
     
    def nextpage(self,bs):
        htmlA = bs.find('a',{'class':'next_page'})
        nextpage = htmlA.get('href')
        return nextpage
        
    def content(self,bs):

        return ''


if __name__ == '__main__':

    h = MyHost()
    h.genNextPageLinks()


# link的输入和输出，系统。获取link，以及添加link了。 
# url和content，都是从页面中解析出来的。也是作为缓存了。所以，需要我们对其可以进行缓存了。以及增加访问标志了。
# 不用正则，而是beautifulsoup就是爽。
