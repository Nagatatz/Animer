# -*- coding: utf-8 -*-

import urllib,urllib2
import sys
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')

class EpgGetter(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        self.content_flag = 0
        self.column_flag = 0
        self.List =[]
        self.str = open('iepg.dat','w')

    def handle_data(self, data): #1
        if self.flag == 1 and self.content_flag == 1:
            self.data = data

            self.str.write(data)
            self.flag = 0
            self.content_flag = 0

    def handle_starttag(self,tagname,attribute): #0
        if tagname.lower() == "a":
            self.flag = 0
            for i in attribute:
                if self.flag == 1:
                    if i[0].lower() == "href":
                        buf = i[1]
                        buf = buf.replace(u'/iepg.tvpi?id=','')
                        self.str.write(buf)
                        self.content_flag = 1
                else:
                    if i[0].lower() == "name":
                        if i[1] == "iepg-button":
                            self.flag = 1

    def Analize(self,url):
        source = urllib2.urlopen(url)
        self.feed(source.read())

        source.close()
        self.str.close()

import datetime

def t2str(x):
    y = x.strftime('%Y%m%d%H%M')
    return y

def nexttime(t):
    s = t + datetime.timedelta(hours =+6 )
    return s

         
def iepgget(t):
    parser = EpgGetter()
    url = 'http://tv.so-net.ne.jp/chart/23.action?head=' + str(t2str(t))
    parser.Analize(url)
    parser.close()
    for line in open('iepg.dat','r'):
        dltvpi(line)
        d = readtvpi('tvpi.dat')
        iepginput(d)

#URL打ち込んでtvpiゲット
def dltvpi(a):
    url = 'http://tv.so-net.ne.jp/iepg.tvpid?id='+ str(a)
    urllib.urlretrieve(url,'tvpi.dat')

import codecs
#tvpi読み込み
def readtvpi(x):
    dic = {}
    for line in codecs.open(x,'r','sjis'):
        if line.find(': ') != -1 :
            name,value = line.replace('\r\n','').split(': ')
            dic[name] = value
        else:
            if dic.has_key('comment'):
                dic['comment']=str(dic['comment']) + line.replace('\r\n','')
            else:
                dic['comment']=line.replace('\r\n','')
    return dic
                

    def Analize(self,url):
        source = urllib2.urlopen(url)
        self.feed(source.read())
        source.close()
        self.str.close()

from .models import Title, Comments
from .models import Program
from django.core.exceptions import ObjectDoesNotExist

def timeset(d,t):
    hh, mm = d[t].split(':')
    k = datetime.datetime(int(d['year']),int(d['month']),int(d['date']),int(hh),int(mm))
    return k

def iepginput(d):
    a_title = Title(name = d['program-title'])
    a_title.save()

    d_comments = Comments(name = d['comment'])
    d_comments.save()

    op = timeset(d,'start')
    ed = timeset(d,'end')
    sg1 = int(d['genre-1']) * 16 + int(d['subgenre-1'])
    sta_dic = {u'ＮＨＫ総合・東京':1,
               u'ＮＨＫＥテレ１・東京':2,
               u'日テレ':4,
               u'テレビ朝日':5,
               u'ＴＢＳ':6,
               u'テレビ東京':7,
               u'フジテレビ':8,
               u'ＴＯＫＹＯ　ＭＸ１':9,
               u'放送大学１':10
               }
    if sta_dic.has_key(d['station-name']):
        c_station = sta_dic[d['station-name']]
    else:
        c_station = 11
    
    wav_dic = {u'DFS00400':1,
               u'DFS00408':2,
               u'DFS00410':4,
               u'DFS00428':5,
               u'DFS00418':6,
               u'DFS00430':7,
               u'DFS00420':8,
               u'DFS05C38':9,
               u'DFS00440':10,
               }
    if wav_dic.has_key(d['station']):
        b_waves = wav_dic[d['station']]
    else:
        b_waves = 11

    if d.has_key('genre-2'):        
        g2 = int(d['genre-2'])
        sg2 = int(d['genre-2']) * 16 + int(d['subgenre-2'])
    else:
        g2 = 16
        sg2 = 256
    x = Program(title = a_title, program_id = d['program-id'], waves = b_waves, station = c_station, start = op, end = ed, gen_1 = d['genre-1'], sgn_1 = sg1, gen_2 = g2, sgn_2 = sg2, comments = d_comments)

    q = Program.objects.filter(station=c_station)
    try:
        q.get(start = op) 
        print x.title
        print' is doubled.'
    except ObjectDoesNotExist:
        x.save()

if __name__ == "__main__":        
    t = datetime.datetime.now()    
    for a in range(27):
        iepgget(t)
        t = t + datetime.timedelta(hours=+6)

def main():
    t = datetime.datetime.now()    
    Program.objects.exclude(start__gt = t).delete()
    for a in range(27):
        s = t
        iepgget(t)
        t = nexttime(s)
