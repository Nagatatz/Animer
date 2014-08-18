# -*- coding: utf-8 -*-

import iepglib
import httpparser
import datetime
from models import Title, Waves, Station, Comments
from models import Program

def timeset(d,t):
    hh, mm = d[t].split(':')
    k = datetime.datetime(d['year'],d['month'],d['date'],hh,mm)
    return k

def iepginput(d):
    a_title = Title(name = d['program-title'])
    b_waves = Waves(name = d['station'])
    c_station = Station(name = d['station-name'])
    d_comments = Comments(name = d['comment'])
    op = timeset(d,start)
    ed = timeset(d,end)
    sg1 = d['genre-1'] * 16 + d['subgenre-1']
    if d['genre-2'] == 0:
        x = Program(title = a_title, program_id = d['program-id'], waves = b_waves, station = c_station, start = op, end = ed, gen_1 = d['genre-1'], sgn_1 = sg1, comments = d_comments)
        x.save
    else :
        sg2 = d['genre-2'] * 16 + d['subgenre-2']
        x = Program(title = a_title, program_id = d['program-id'], waves = b_waves, station = c_station, start = op, end = ed, gen_1 = d['genre-1'], sgn_1 = sg1, gen_2 = d['genre-2'], sgn_2 = sg2, comments = d_comments)
        x.save
         
def iepgget(t):
    url = 'http://tv.so-net.ne.jp/chart/23.action?head=' + iepglib.t2str(t)
    httpparser.EpgGetter.Analize(url)
    for line in open('iepg.dat','r'):
        iepglib.dltvpi(line)
        d = iepglib.readtvpi('tvpi.dat')
        iepginput(d)

if __name__ == "__main__":        
    t = datetime.datetime.now()    
    for a in range(27):
        iepgget(t)
        t = t + timedelta(hours=+6)
