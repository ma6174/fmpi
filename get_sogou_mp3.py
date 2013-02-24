#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import re
def getlink(music_name):
    quote_name = urllib.quote(music_name.decode('utf-8').encode('gbk'))
    query_url = 'http://mp3.sogou.com/music.so?query=%s&class=1&pf=&w=02009900&st=&ac=1&sourcetype=sugg&_asf=mp3.sogou.com&_ast=1361525645'%quote_name
    data = urllib2.urlopen(query_url,timeout=10).read()
    re_com = re.compile('onclick="window.open\(\'(.*?)\'')
    forward_links = re_com.findall(data)
    total = len(forward_links)
    if total == 0:
        return None
    for i in range(total):
        next_link = "http://mp3.sogou.com"+forward_links[i]
        data2 = urllib2.urlopen(next_link,timeout=10).read()
        re_com2 = re.compile('<div class="dl"><a href=\"(.*?)\"')
        download_link = re_com2.findall(data2)
        try:
            if download_link[0][-3:] == 'mp3':
                return download_link[0]
        except:
            pass
    return None

def get_all_mp3(url):
    '''get all mp3 from a url'''
    data = urllib2.urlopen(url).read()
    re_com = re.compile('http://.*?\.mp3')
    all = re_com.findall(data)
    re_com = re.compile('<a href=\"(.*?\.mp3)\"')
    ll = re_com.findall(data)
    for i in ll:
        if urllib.basejoin(url,i) not in all:
            all.append(urllib.basejoin(url,i))
    return list(set(all)) #删除重复歌曲

if __name__=='__main__':
    print getlink('滴答')
