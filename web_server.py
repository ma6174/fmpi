#!/usr/bin/env python
#coding=utf-8
import web
import logging
from fmpi import FMPI
from threading import Thread
urls = (
    '/',"INDEX",
)
app = web.application(urls,globals())
web.config.debug = False
pi = FMPI()

class INDEX(FMPI):
    '''web页面相关'''
    def index(self):
        html = '''<head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="/static/favicon.ico" >
        </head>
        <html>
        <form action="/" method="GET">
        music path or url:
        <input type="TEXT" name="m" />
        <input type="submit" value="play"  />
        </from>
        </html>
         '''
        return html

    def GET(self,args=None):
        input = web.input()
        if input.has_key('m'):
            key = input['m']
            logging.info("play %s"%key)
            pi.play(key)
        return self.index()

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    app.run() #web服务器--主线程
