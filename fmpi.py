#!/usr/bin/env python
#coding=utf-8

import os
import web
import time
import sqlite3
from threading import Thread
from get_sogou_mp3 import getlink
import locale 
locale.setlocale(locale.LC_ALL, '') 

urls = (
    '/',"INDEX",
)
app = web.application(urls,globals())
#web.config.debug = False

class DB:
    '''数据库相关操作'''
    db_name = "query.db"
    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        sql_create = '''create table if not exists music(
        id integer primary key autoincrement,
        title text,
        status text
        )'''
        cur.execute(sql_create)
        conn.commit()
        cur.close()
        conn.close()
        return 0
    def put(self,music_name):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        sql_insert = 'insert into music(title,status) values ("%s","%s")'%(music_name,"wait")
        cur.execute(sql_insert)
        conn.commit()
        cur.close()
        conn.close()
        return 0
    def getall(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        sql_select = 'select id,title from music where status = "wait"'
        cur.execute(sql_select)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    def updateone(self,id):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        sql_update = 'update music set status = "done" where id = %s'%id
        cur.execute(sql_update)
        conn.commit()
        cur.close()
        conn.close()
        return 0


class FMPI(DB):
    '''从播放队列获取歌曲并播放'''
    def play(self,name_or_url,freq=97.5,rate=44100):
        '''调用外部播放命令'''
        cmd = "mpg123 -m -C -q -s %s |sudo pifm - %s %s"%(name_or_url,freq,rate)
        print cmd
        os.system(cmd)
        return 0
    def fmpi(self):
        '''循环检测'''
        while True:
            query = DB.getall(self)
            try:
                one = query[0]
            except:
                one = None
            if one is not None:
                url = getlink(one[1])
                self.play(url)
                DB.updateone(self,one[0])
            time.sleep(1)#降低CPU占用率

class INDEX(DB):
    '''web页面相关'''
    def index(self):
        html = '''<head><meta charset="UTF-8"></head>
        <html>
        <form action="/" method="GET">
        I want to listen:
        <input type="TEXT" name="m" />
        <input type="submit" value="submit"  />
        </from>
         '''
        query = DB.getall(self)
        try:
            html += u"<h2>Playing</h1>%s<h2>list</h1>"%query[0][1]
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
    def GET(self,args=None):
        input = web.input()
        try:
            music_name = input['m']
            print music_name
        except:
            print "no input"
            return self.index()
        if self.check_name_exist(music_name) is False:
            DB.put(self,music_name)
            raise web.seeother('/')
        else:
            return '''<head><meta charset="UTF-8"></head>
            <h1>music already exists'''

if __name__=='__main__':
    db = DB()
    db.create_table()
    pi = FMPI()
    player = Thread(target=pi.fmpi) #播放线程在后台
    player.setDaemon(True)     #随主线程一块退出
    player.start()
    app.run() #启动web服务器
