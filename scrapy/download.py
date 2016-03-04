# -*- coding: utf-8 -*-

import urllib2
import time

from lab.header import update_header
from lab.opener import mixUrllib2
from utils.ip import proxyip

if __name__ == '__main__':
    url = 'http://www.oschina.net/code/snippet_2463131_51169'
    request = urllib2.Request(url)
    request = update_header(request)
    
    for pstr in proxyip(1):
        content = mixUrllib2(pstr).urlopen(request)
        print content.read().decode("utf8")  
        time.sleep(2)

# Scrapple 是一个用来开发 Web 爬虫程序的 Python 框架，使用 key-value 配置文件。
# 一个基于gevent的爬虫框架，最初的版本在一定程度上模仿了scrapy。
# PySipder 是一个 Python 爬虫程序

# 演示地址：http://demo.pyspider.org/
#    强大的 WebUI 和脚本编辑器、任务监控和项目管理和结果查看
#    后端系统支持：MySQL, MongoDB, SQLite, Postgresql
#    支持任务优先级、重试、定期抓取等
#    分布式架构

# 学习爬虫，学习技术。
# 对于proxy端口，扫描端口，检测端口是否可用了。 返回可用的端口。

# Portia是scrapyhub开源的一款可视化的爬虫规则编写工具。它提供可视化的Web页面，你只需要通过点击标注页面上你需要抽取的数据，不需要任何编程知识即可完成规则的开发。

# 分布式爬虫框架 Cola
# 分布式视频信息爬虫 videoSpider
# 番号种子采集器 

# 增加连接池，目前看，比较困难了。 或者缓存squid
# 使用Selenium调用浏览器扒取页面
# 爬虫之前产生代理列表缓存，然后怕取每个link时随机使用代理IP， 爬取link时随机使用代理列表了。

# tornado 异步爬取了。是的。 

# urllib2,requests,re,BeautifulSoup,scrapy,PIL,opencv,pybrain,threading,celery

# 使用requests ，而非urllib2

# 安全工作大致也就是如此了。是的。
# 虚拟机使用高匿代理安全，所有的数据都是要过这些的端口的。所以重要的数据，不要使用。

# 高匿网站IP 解析。通过自动化连接。获取到link了。
# 针对主机的情况，面向对像了。是的。不同的网站，会选择继承了。是的。

# 采用先写框架，比如说随机代理，分布式框架，缓存等。先把这些的内容搞定了，然后就可以了。以及异步等。是的。
# 读源码，是要耗费更多的精力的。是的。
