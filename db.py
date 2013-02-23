#!/usr/bin/env python
#coding=utf-8
import sqlite3
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
