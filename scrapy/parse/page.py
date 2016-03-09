# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from BeautifulSoup import BeautifulSoup

class Page(object):
    def __init__(self,html,url,classes,uuid):
        self.f = BeautifulSoup(html)
        self.positionclasses = classes
        self.uuid = uuid

    def parse(self):
        for position_class in self.positionclasses:
            position_class(self.f,self.uuid).parse()
   
if __name__ == '__main__':

    page = Page(file('html.txt').read(),'www.xicidaili.com',[],'') 
    page.parse()

