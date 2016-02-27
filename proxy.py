# -*- coding:utf8 -*-
import requests
import re
import time
from BeautifulSoup import BeautifulSoup
of = open('proxy.txt', 'w')
url = 'http://www.haodailiip.com/guonei/'
for i in range(1,20):
    Url = 'http://www.haodailiip.com/guonei/' + str(i)
    print "正在采集"+Url
    html = requests.get(Url).text
    bs = BeautifulSoup(html)
    table = bs.find('table',{"class":"proxy_table"})
    tr = table.findAll('tr')
    for i in range(1,31):
        td = tr[i].findAll('td')
        proxy_ip = td[0].text.strip()
        proxy_port = td[1].text.strip()
        of.write('http=%s:%s\n' %(proxy_ip,proxy_port))
        print 'http=%s:%s\n' %(proxy_ip,proxy_port)
    time.sleep(2)
of.closed

