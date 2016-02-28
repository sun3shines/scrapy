# -*- coding:utf8 -*-

import requests
import re
import time
from BeautifulSoup import BeautifulSoup
import socket

def genRandomIP():
    pass

def genProxyIP():
    rootdir = '/root/scrapy/utils'
    url = 'http://www.haodailiip.com/guonei/'

    hostName = url.replace('http://','').split('/')[0].replace('.','')
    path = rootdir + '/' + 'anonymous' + '/' + hostName 
    of = open(path,'w')

    for i in range(1,20):
        Url = 'http://www.haodailiip.com/guonei/' + str(i)
        print "正在采集"+Url

        resp = requests.get(Url)
        html = resp.text
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

                                                                                                                                                                                                                                            
def proxyip(num):

    socket.setdefaulttimeout(2)

    n = 0
    try:
        handle = file('/root/scrapy/utils/proxy.txt')
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if not isActive(line):
                continue
            if n >= num:
                break
            yield line.strip().replace('=','://')   
            n = n + 1
    finally:
        handle.close()

def isActive(pstr):
    # aa = 'http=27.44.168.26:9999'
    host = pstr.split('=')[1].split(':')[0]
    port = pstr.split('=')[1].split(':')[1]
    # http=203.195.172.147:8080
    # 'http://XX.XX.XX.XX:XXXX' 
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((host,int(port)))
        sock.shutdown(2) 
        return True
    except:
        sock.close()
        return False

def genLinks():

    rootdir = '/root/scrapy/utils'
    StartUrl = 'http://www.xicidaili.com/wn/'
    prefix = 'http://www.xicidaili.com'

    hostName = prefix.replace('http://','').split('/')[0].replace('.','')
    path = rootdir + '/' + 'anonymous' + '/' + hostName
    headers =  {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
                'Host':'www.xicidaili.com'}

    queuehrefs = []
    queuehrefs.append(StartUrl)
    while len(queuehrefs) > 0:
        url = queuehrefs.pop(0)
        print url
        resp = requests.get(url,headers=headers)
        html = resp.text
        bs = BeautifulSoup(html)

        htmlA = bs.find('a',{'class':'next_page'}) 
        nextLink = htmlA.get('href')

        if nextLink in queuehrefs:
            continue
        queuehrefs.append(prefix+nextLink)
        time.sleep(1)

if __name__ == '__main__':
 
#    for ip in proxyip(10):
#        print ip
#     genProxyIP()

    genLinks()
# <a class="next_page" rel="next" href="/wn/2">下一页 ›</a>
# 通过next_page 过滤是不是更好。那么现在就是发现所有的netxt_page
# 解析出来详细的信息。以及requests如何使用代理？
# 链接获取方式，一种是页面的next_page的方式，一种是页面的所有的链接了。
# 先搭建框架。为每个不同的网站，写不同的代码了。比如说获取link的代码等等。是的。
 
