# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from BeautifulSoup import BeautifulSoup
from scrapy.elm.haodailiip.position import Link,Content
class Page(object):
    def __init__(self,html):
        self.f = BeautifulSoup(html)
        try:
#            file('html.txt','w').write(html)
             pass
        except:
            pass

    def getpostions(self):
        return [Link,Content]
    
    def parse(self):
        for position_class in self.getpostions():
            position_class(self.f).parse()
   
if __name__ == '__main__':

    page = Page(file('html.txt').read()) 
    page.parse()

