
from scrapy.common.task import Task
import requests

class Url(Task):
    
    def __init__(self,host,port,url,p=True):
        self.host = host
        self.port = port
        self.url = url.replace('http://','').replace('http:/','')
        self.agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'
        self.timeout = 25
        if p: 
            self.proxyget()
        else:
            self.get()

    def getProxy(self):
        return {"http": "http://%s:%s" % (self.host,self.port)}

    def getMethod(self):
        return 'GET'
    
    def getUrl(self):
        return 'http://'+self.url

    def getHeaders(self):
        return {'User-Agent':self.agent}

    def get(self):
        self.resp = requests.get(self.getUrl(),headers=self.getHeaders(),timeout=self.timeout)

    def proxyget(self):   
        self.resp = requests.get(self.getUrl(),headers=self.getHeaders(),proxies=self.getProxy(),timeout=self.timeout)

    @property
    def html(self):
        return self.resp.text

    @property
    def status(self):
        return self.resp.status_code

if __name__ == '__main__':

    ip = '122.96.59.104'
    port = '80'
    u = Url(ip,port,'http://mm3825.com/html/article/index12056.htm',p=False)   

    print u.status
    print u.html
 
