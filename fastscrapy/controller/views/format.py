# -*- coding: utf-8 -*-

def filter(attrs):
    # [{u'url': u'1457154733.35', u'state': 0, u'id': 75, u'proxy': {u'active': 1, u'ip': u'123.157.99.140', u'id': 58, u'port': 8000}}
    newattrs = []
    for attr in attrs:
        attr.pop('state')
        attr.get('proxy').pop('id')
        attr.get('proxy').pop('active')
        newattrs.append(attr)
    return newattrs

def printattrs(pid,attrs):
    print '* * * * * * * * * * %s * * * * * * * * * * *\n' % (pid)
    debugs = ' , '.join([str(attr['id'])for attr in attrs])
    print debugs

    print '\n'
