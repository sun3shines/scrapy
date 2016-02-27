
import urllib2
import time

if __name__ == '__main__':
    url = 'http://www.oschina.net/code/snippet_2463131_51169'
#    content = urllib2.urlopen(url).read()
#    print content
    
#    url = 'http://www.xicidaili.com/nn/%s' %page
    user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    request = urllib2.Request(url)
    request.add_header("User-Agent", user_agent)
    content = urllib2.urlopen(request)

    print content.read()

    time.sleep(2)
