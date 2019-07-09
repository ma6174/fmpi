#!/usr/bin/env python
# coding=utf-8
import time
import config
import logging
import subprocess

class FMPI():
    def play(self, name_or_url, freq=98.5, rate=44100):
        '''调用外部播放命令'''
# cmd = "mpg123 -m -C -q -s %s | sudo pifm - %s
# %s"%(name_or_url,freq,rate)
        cmd1 = "mpg123 -m -C -q -s %s" % name_or_url
        cmd2 = "sudo pifm - %s %s" % (freq, rate)
        self.p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
        self.p2 = subprocess.Popen(
            cmd2,
            shell=True,
            stdin=self.p1.stdout,
            stdout=subprocess.PIPE)
        self.p1.wait()
        return 0
