# -*- coding: utf-8 -*-

import MySQLdb

class dbConn(object):

    def __init__(self,host,user,passwd,port,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.flag = False

    def connect(self):
        
        if not self.flag:
            self.connection = MySQLdb.connect(host=self.host,user=self.user,
                                              passwd=self.passwd,port=self.port,db=self.db) 
            self.flag = True

    def close(self):

        if self.flag:
            self.connection.close()
            self.flag = False

    def getData(self,sqlStr):
        self.connect()
        cur = self.connection.cursor()
        cur.execute(sqlStr)
        data = cur.fetchone()
        cur.close()
        self.connection.commit()
        return data

    def getDataList(self,sqlStr):

        self.connect()
        cur = self.connection.cursor()
        cur.execute(sqlStr)
        data = cur.fetchall()
        cur.close()
        self.connection.commit()
        return data

    def genAttrsStr(self,attrs):
        
        return ' , '.join(attrs)
    
    def genConditionStr(self,cdict):

        cs = ["%s = '%s'" % (str(key),str(cdict[key])) for key in cdict]
        return ' and '.join(cs)
    
    def genValsStr(self,vals):
        
        vs = ["'%s'" % (v) for v in vals]
        
        return ' , '.join(vs)
    
    def select(self,attrs,table,c={},e = ''):

        attrsStr = self.genAttrsStr(attrs)
        
        sqlStr = 'select %s from %s' % (attrsStr,table)
        if c:
            conditionStr = self.genConditionStr(c)
            sqlStr = sqlStr + ' where %s' % (conditionStr)
             
        if e:
            sqlStr = sqlStr + e
            
        return self.getDataList(sqlStr)
         
    def execute_sql(self,sqlStr):

        self.connect()
        cur = self.connection.cursor()
        cur.execute(sqlStr)
        cur.close()
        self.connection.commit()

    def genUpdateValStr(self,s):
        
        ss = ["%s = '%s'" % (str(key),str(s[key])) for key in s]
         
        return ' , '.join(ss)
    
    def update(self,s,t,c,e=''):

        sStr = self.genUpdateValStr(s)
        sqlStr = 'update %s set %s ' % (t,sStr)
        if c:
            cStr = self.genConditionStr(c)
            sqlStr = sqlStr + ' where %s' % (cStr)
        
        if e:
            sqlStr = sqlStr + e
            
        self.execute_sql(sqlStr)
        return True,''
    
    def insert(self,attrs,vals,table):
        
        attrsStr = self.genAttrsStr(attrs)
        valsStr = self.genValsStr(vals)
        sqlStr = 'insert into %s (%s) values (%s)' % (table,attrsStr,valsStr)
        self.execute_sql(sqlStr) 
        return True,''
   
    def delete(self,table,condition):
        
        sqlStr = 'delete from %s' % (table)
        if condition:
            conditionStr = self.genConditionStr(condition)
            sqlStr = sqlStr + ' where %s' % (conditionStr)
        self.execute_sql(sqlStr)
                
        return True,''
     
    def splitPath(self,absPath):

        return absPath.split('/')[-1],'/'.join(absPath.split('/')[:-1])

def getDb():

    return dbConn('192.168.36.3','root','111111',3306,'scrapy')
