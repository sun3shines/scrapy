
import time

def getpage(attrs):
    
    surls = {}
    for attr in attrs:
        id = attr['id']
        surls[id] = []
        time.sleep(1.5)
        surls[id].append(str(time.time()))
        time.sleep(1.5)
        surls[id].append(str(time.time()))
        
    return surls
