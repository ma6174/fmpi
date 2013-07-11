#!/usr/bin/env python
# coding=utf-8
#!/usr/bin/python
# coding: utf-8

import httplib
import json
import sys
import subprocess
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def getmusic():
    httpConnection = httplib.HTTPConnection('douban.fm')
    httpConnection.request('GET', '/j/mine/playlist?type=n&channel=0')
    song = json.loads(httpConnection.getresponse().read())['song']
    return song[0]

if __name__ == '__main__':
    while True:
        song = getmusic()
        print song['title'], song['artist'], song['albumtitle']
        player = subprocess.Popen('mpg123 -C %s' % song['url'], shell=True)
        time.sleep(song['length'])
        player.kill()
