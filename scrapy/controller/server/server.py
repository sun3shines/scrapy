# Copyright (c) 2010-2012 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import with_statement

import os
import time
import traceback
from urllib import unquote
from xml.sax import saxutils

from eventlet import Timeout
from webob import Request, Response

from cloudcommon.common.utils import get_logger,  public
from cloudcommon.common.constraints import check_utf8
from cloudcommon.common.bufferedhttp import jresponse

from ufs.route.urls import handlerequest

class ServerController(object):
    """WSGI controller for the account server."""

    def __init__(self, conf):
        self.logger = get_logger(conf, log_route='cloud-server')
        
    def __call__(self, env, start_response):
        req = Request(env)
        
        self.logger.txn_id = req.headers.get('x-trans-id', None)
        if not check_utf8(req.path_info):
            res = jresponse('-1', 'invalid utf8', req,412)
        else:
            try:
                res = handlerequest(req) 
            except (Exception, Timeout):
                self.logger.exception(_('ERROR __call__ error with %(method)s'
                    ' %(path)s '), {'method': req.method, 'path': req.path})
                res = jresponse('-1', 'InternalServerError', req,500)
                
        return res(env, start_response)

def app_factory(global_conf, **local_conf):
    """paste.deploy app factory for creating WSGI account server apps"""
    conf = global_conf.copy()
    conf.update(local_conf)
    return ServerController(conf)

