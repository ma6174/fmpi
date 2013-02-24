#!/usr/bin/env python
#coding=utf-8
import web
from db import DB
from fmpi import FMPI
from mylog import Log
from threading import Thread
urls = (
    '/',"INDEX",
)
app = web.application(urls,globals())
web.config.debug = False


class INDEX(DB,FMPI):
    '''web页面相关'''
    def index(self):
        html = '''<head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="/static/favicon.ico" >
        </head>
        <html>
        <form action="/" method="GET">
        I want to listen:
        <input type="TEXT" name="m" />
        <input type="submit" value="add to list"  />
        </from>
         '''
        query = DB.getall(self)
        try:
            html += u"<h2>Now Playing</h1>%s<h2>list to be played</h1>"%query[0][1]
            num = 1
            for i in query[1:]:
                html = html + '<li>%d----%s</li>'%(num,i[1])
                num+=1
            return html
        except:
            return html
    def check_name_exist(self,name):
        '''检查歌曲名字是否存在'''
        all = DB.getall(self)
        for i in all:
            print i[1]
            if i[1] == name:
                return True
        return False
    def add_music(self,music_name):
        if self.check_name_exist(music_name) is False:
            DB.put(self,music_name)
            return None
        else:
            return '''<head><meta charset="UTF-8"></head>
            <h1>music already exists'''

    def GET(self,args=None):
        input = web.input()
        if input.has_key('c'):
            key = input['c']
#            FMPI.control(self,key)
            web.seeother('/')
        if input.has_key('m'):
            music_name = input['m']
            ret = self.add_music(music_name)
            if ret is None:
                web.seeother('/')
            else:
                return ret
        return self.index()

if __name__=='__main__':
    db = DB()
    db.create_table()
    pi = FMPI()
    player = Thread(target=pi.fmpi) #播放器线程
    player.setDaemon(True)     #随主线程一块退出
    player.start()
    app.run(Log) #web服务器--主线程
