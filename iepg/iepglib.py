# -*- coding: utf-8 -*-

from datetime

def t2str(x):
    y = x.strftime('%Y%m%d%H%M')
    return y

def nexttime(t):
    t = t + timedelta(hours = +1)
    return t

import urllib
#URL打ち込んでtvpiゲット
def dltvpi(a):
    url = 'http://tv.so-net.ne.jp/iepg.tvpi?id='+ str(a)
    urllib.urlretrieve(url,'tvpi.dat')
    return 0


import codecs
#tvpi読み込み
def readtvpi(x):
    dic = {}
    for line in codecs.open(x,'r','sjis'):
        if line.find(':') != -1 :
            name, value = line.replace('\r\n','').split(': ')
            dic[name] = value
        else:
            dic['comment']=line.replace('\r\n','')
    return dic
