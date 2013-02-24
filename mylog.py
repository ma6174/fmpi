#!/usr/bin/env python
#coding=utf-8

#import sys, logging
from wsgilog import WsgiLog
#import config

class Log(WsgiLog):
    def __init__(self, application):
        WsgiLog.__init__(
            self,
            application,
            logformat = '%(message)s',
#            tofile = True,
            toprint = True,
#            file = config.log_file,
#            interval = config.log_interval,
#            backups = config.log_backups
        )
