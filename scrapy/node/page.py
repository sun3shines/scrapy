# -*- coding: utf-8 -*-
import time

def getpage(attrs):
    print attrs    
    finishurls = []
    for attr in attrs:   
        id = attr['id']
        url = attr['url']
        proxyhost = attr['proxy']['ip']
        proxyport = attr['proxy']['port']
        print id,url,proxyhost,proxyport 
        # tr = Thread(url,host,port)
        # tr.start()
        # tr.join()
        finishurls.append(id)
    return finishurls


# 任务分发，任务处理，任务存储。

# 对于结果需要收集的。进行一个任务转发。比如说linkpostion，和proxypostion了。是的。

# 以id和url作为每个position中的唯一标志符了。是的。

# 对于新的结果处理方式，我看还是要分开的好。只是返回需要处理的。id了，表示此id已完成了。但是可以慢慢发了。

# 因此，还是putget一体了。以及，我们的任务处理从我们的进程管理中脱离出来了。是的。

# putget 不涉及到结果的回首和处理了。而结果的回首处理由xx来进行了。是的。 这个很重要。把link作为结果，从put/get中解脱处理，这样就简单多了。是的。单纯的读和修改了。

# 以及link的插入操作，会被作为merget来处理了。是的以及proxy的merget来处理了。的。

# 所以，现在需要开一个线程了。增加对于link和proxy的merget了。是的。分离主义。分离主义，要更加的模块化了。是的。

# 但是，进程会等待所有的任务都完成了。是的。所以说进程和线程还是有管理了。因为进程必须等待线程完成后，自己才能去做其他的事情了。是的。

# 增加datamerget 的各种后台线程了。是的。除了link，和proxy是线程。其他的merget，可以作为进程来处理了。是的。

# 因此，我们可以这样理解。即link的增加，不归dispatch所管。而是由新的模块来负责。其只负责减少了。是的。负责消耗未完成的ids了。完成，继续请求，继续消耗了。是的。
