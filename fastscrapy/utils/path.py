# -*- coding: utf-8 -*-

def urlpath(path):

    n = []
    for p in path.split('/'):
        if not p:
            continue
        n.append(p)
    return '/'.join(n)




