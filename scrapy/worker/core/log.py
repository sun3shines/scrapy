
import syslog

def logfork(pid):
    syslog.syslog(syslog.LOG_ERR,'fork process: '+pid)
    
def logexit(pid):
    syslog.syslog(syslog.LOG_ERR,'exit process: '+pid)

def logurls(pid,ids):
    syslog.syslog(syslog.LOG_ERR,'urls process: '+pid +'  '+ str(ids))

def logerror(pid,msg):
    syslog.syslog(syslog.LOG_ERR,'erro process: '+pid +'  '+str(msg))