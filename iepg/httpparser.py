import urllib2
import sys
from HTMLParser import HTMLParser

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
                        buf = buf.replace('/iepg.tvpi?id=','')
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

if __name__ == "__main__":
    parser = EpgGetter()
    parser.Analize('http://tv.so-net.ne.jp/chart/23.action?head=201309221300')
    parser.close()
