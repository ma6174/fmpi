#!/usr/bin/env python
#coding=utf-8

import os
import time
import random
from db import DB
from get_sogou_mp3 import getlink

class FMPI(DB):
    '''从播放队列获取歌曲并播放'''
    def play(self,name_or_url,freq=97.5,rate=44100):
        '''调用外部播放命令'''
        cmd = "mpg123 -m -C -q -s %s |sudo pifm - %s %s"%(name_or_url,freq,rate)
        print cmd
        os.system(cmd)
        return 0

    def get_random_music(self):
        music_set = file("./music_name.txt").readlines()
        total = len(music_set)
        rand = random.randint(0,total-1)
        return music_set[rand][:-1]

    def fmpi(self):
        '''循环检测'''
        while True:
            query = DB.getall(self)
            try:
                one = query[0]
            except:
                one = None
            if one is not None:
                url = getlink(one[1].encode('utf-8'))
                self.play(url)
                DB.updateone(self,one[0])
            else:
                rand_music = self.get_random_music()
                DB.put(self,rand_music)
            time.sleep(1)#降低CPU占用率

