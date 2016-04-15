
import urllib2
import cookielib

def CookieUrllib2():

    cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())  
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
    urllib2.install_opener(opener)  
    return urllib2



