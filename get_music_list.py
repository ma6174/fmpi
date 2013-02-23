#!/usr/bin/env python
#coding=utf-8
import urllib2
import re
def get_music():
    url = 'http://list.mp3.baidu.com/top/top5001.html'
    data = urllib2.urlopen(url).read().decode('gbk').encode('utf-8')
    re_com = re.compile('\]\)\" >(.*)</a></div>')
    all = re_com.findall(data)
    write_to_file = ""
    for i in all:
        print i
        write_to_file = "%s\n%s"%(write_to_file,i)
    print write_to_file
    file('music_name.txt','w').write(write_to_file)

if __name__ == '__main__':
    get_music()
