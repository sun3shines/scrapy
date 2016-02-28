# -*- coding: utf-8 -*-

def update_header(req):

    # host = req._Request__original.split('/')[0]
    # user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    # req.add_header("User-Agent", user_agent)
   
    req.add_header('Referer','http://www.cnbeta.com/articles')
    req.add_header('X-Forwarded-For','3.3.3.3')

# firefox

    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    # req.add_header('Accept-Encoding','gzip, deflate') 
    req.add_header('Accept-Language',' zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    # req.add_header('Connection','keep-alive')
    req.add_header('DNT','1')
    # req.add_header('Host',host)
    req.add_header('User-Agent',' Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')

    return req

# 学习使用httpfox，研究看到的header了。

# 再不行，那就只能用终极绝招了，selenium直 接控制浏览器来进行访问，只要浏览器可以做到的，那么它也可以做到。类似的还有pamie，watir，等等等等。

# 反盗链
# 伪装浏览器


# 能够直接模拟ajax请求获取数据固然是极好的，但是有些网站把ajax请求的所有参数全部加密了。我们根本没办法构造自己所需要的数据的请求。我这几天爬的那个网站就是这样，除了加密ajax参数，它还把一些基本的功能都封装了，全部都是在调用自己的接口，而接口参数都是加密的。遇到这样的网站，我们就不能用上面的方法了，我用的是selenium+phantomJS框架，调用浏览器内核，并利用phantomJS执行js来模拟人为操作以及触发页面中的js脚本。从填写表单到点击按钮再到滚动页面，全部都可以模拟，不考虑具体的请求和响应过程，只是完完整整的把人浏览页面获取数据的过程模拟一遍。
