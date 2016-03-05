
import threading

from scrapy.controller.db.table.mysql import dbConn

class db(dbConn):
    def __init__(self,*args, **kwargs):
        
        super(db,self).__init__(*args, **kwargs)
        self.dblock = threading.Lock()
        
    def lock(self):
        return self.dblock.acquire()
    
    def unlock(self):
        self.dblock.release()

class LOCK:
    def __init__(self,conn):
        self.conn = conn

    def __enter__(self):
        self.conn.lock()
        return self

    def __exit__(self,type,value,trace):
        self.conn.unlock()

def getlock(conn):

    return LOCK(conn)
      
def getdb():

    return db('192.168.36.3','root','111111',3306,'scrapy')

conn = getdb()
