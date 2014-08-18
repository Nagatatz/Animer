# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Favorites(models.Model):
    user = models.ForeignKey(User, unique=True)
    #favorite of channels
    fav_ch01 = models.BooleanField() #NHK
    fav_ch02 = models.BooleanField() #NHK_E
    fav_ch04 = models.BooleanField() #NTV
    fav_ch05 = models.BooleanField() #ASAHI
    fav_ch06 = models.BooleanField() #TBS
    fav_ch07 = models.BooleanField() #TX
    fav_ch08 = models.BooleanField() #CX
    fav_ch09 = models.BooleanField() #MX
    fav_ch10 = models.BooleanField() #OUJ
    #favorite of gennres
    fav_gn00 = models.BooleanField() #news
    fav_gn01 = models.BooleanField() #sports
    fav_gn02 = models.BooleanField() #infomation
    fav_gn03 = models.BooleanField() #drama
    fav_gn04 = models.BooleanField() #music
    fav_gn05 = models.BooleanField() #variety
    fav_gn06 = models.BooleanField() #cinema
    fav_gn07 = models.BooleanField() #anime/VFX
    fav_gn08 = models.BooleanField() #documentary/liberal arts
    fav_gn09 = models.BooleanField() #theatre
    fav_gn10 = models.BooleanField() #hobby/education
    fav_gn11 = models.BooleanField() #welfare
    fav_gn15 = models.BooleanField() #other

    class Meta:
        pass

    def __unicode__(self):
        return self.user.username

class Title(models.Model):
    name = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name

#class Waves(models.Model):
#    name = models.CharField(max_length=10)
#    def __unicode__(self):
#        return self.name

#class Station(models.Model):
#    name = models.CharField(max_length=20)
#    def __unicode__(self):
#        return self.name

class Comments(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Program(models.Model):
    GENRE_CHOICES = (
        (0,u'ニュース／報道'),
        (1,u'スポーツ'),
        (2,u'情報／ワイドショー'),
        (3,u'ドラマ'),
        (4,u'音楽'),
        (5,u'バラエティ'),
        (6,u'映画'),
        (7,u'アニメ／特撮'),
        (8,u'ドキュメンタリー／教養'),
        (9,u'劇場／公演'),
        (10,u'趣味／教育'),
        (11,u'福祉'),
        (15,u'その他'),
        (16,u'なし'),
        )
    SUBGEN_CHOICES = (
         (0,u'定時・総合'),
         (1,u'天気'),
         (2,u'特集・ドキュメント'),
         (3,u'政治・国会'),
         (4,u'経済・市況'),
         (5,u'海外・国際'),
         (6,u'解説'),
         (7,u'討論・会談'),
         (8,u'報道特番'),
         (9,u'ローカル・地域'),
         (10,u'交通'),
         (15,u'ニュース／報道-その他'),

         (16,u'スポーツニュース'),
         (17,u'野球'),
         (18,u'サッカー'),
         (19,u'ゴルフ'),
         (20,u'その他の球技'),
         (21,u'相撲・格闘技'),
         (22,u'オリンピック・国際大会'),
         (23,u'マラソン・陸上・水泳'),
         (24,u'モータースポーツ'),
         (25,u'マリン・ウィンタースポーツ'),
         (26,u'競馬・公営競技'),
         (31,u'スポーツ-その他'),

         (32,u'芸能・ワイドショー'),
         (33,u'ファッション'),
         (34,u'暮らし・住まい'),
         (35,u'健康・医療'),
         (36,u'ショッピング・通販'),
         (37,u'グルメ・料理'),
         (38,u'イベント'),
         (39,u'番組紹介・お知らせ'),
         (47,u'情報／ワイドショー-その他'),

         (48,u'国内ドラマ'),
         (49,u'海外ドラマ'),
         (50,u'時代劇'),
         (63,u'ドラマ-その他'),

         (64,u'国内ロック・ポップス'),
         (65,u'海外ロック・ポップス'),
         (66,u'クラシック・オペラ'),
         (67,u'ジャズ・フュージョン'),
         (68,u'歌謡曲・演歌'),
         (69,u'ライブ・コンサート'),
         (70,u'ランキング・リクエスト'),
         (71,u'カラオケ・のど自慢'),
         (72,u'民謡・邦楽'),
         (73,u'童謡・キッズ'),
         (74,u'民族音楽・ワールドミュージック'),
         (79,u'音楽-その他'),

         (80,u'クイズ'),
         (81,u'ゲーム'),
         (82,u'トークバラエティ'),
         (83,u'お笑い・コメディ'),
         (84,u'音楽バラエティ'),
         (85,u'旅バラエティ'),
         (86,u'料理バラエティ'),
         (95,u'バラエティ-その他'),

         (96,u'洋画'),
         (97,u'邦画'),
         (98,u'アニメ映画'),
         (111,u'映画-その他'),

         (112,u'国内アニメ'),
         (113,u'海外アニメ'),
         (114,u'特撮'),
         (127,u'アニメ／特撮-その他'),

         (128,u'社会・時事'),
         (129,u'歴史・紀行'),
         (130,u'自然・動物・環境'),
         (131,u'宇宙・科学・医学'),
         (132,u'カルチャー・伝統文化'),
         (133,u'文学・文芸'),
         (134,u'スポーツ'),
         (135,u'ドキュメンタリー全般'),
         (136,u'インタビュー・討論'),
         (143,u'ドキュメンタリー／教養-その他'),

         (144,u'現代劇・新劇'),
         (145,u'ミュージカル'),
         (146,u'ダンス・バレエ'),
         (147,u'落語・演芸'),
         (148,u'歌舞伎・古典'),
         (159,u'劇場／公演-その他'),

         (160,u'旅・釣り・アウトドア'),
         (161,u'園芸・ペット・手芸'),
         (162,u'音楽・美術・工芸'),
         (163,u'囲碁・将棋'),
         (164,u'麻雀・パチンコ'),
         (165,u'車・オートバイ'),
         (166,u'コンピュータ・ＴＶゲーム'),
         (167,u'会話・語学'),
         (168,u'幼児・小学生'),
         (169,u'中学生・高校生'),
         (170,u'大学生・受験'),
         (171,u'生涯教育・資格'),
         (172,u'教育問題'),
         (175,u'趣味／教育-その他'),

         (176,u'高齢者'),
         (177,u'障害者'),
         (178,u'社会福祉'),
         (179,u'ボランティア'),
         (180,u'手話'),
         (181,u'文字（字幕）'),
         (182,u'音声解説'),
         (191,u'福祉-その他'),

         (255,u'その他-その他'),
         (256,u'なし'),
        )
    STATION_CHOICES = (
        (1,u'ＮＨＫ総合・東京'),
        (2,u'ＮＨＫＥテレ１・東京'),
        (4,u'日テレ'),
        (5,u'テレビ朝日'),
        (6,u'ＴＢＳ'),
        (7,u'テレビ東京'),
        (8,u'フジテレビ'),
        (9,u'ＴＯＫＹＯ　ＭＸ１'),
        (10,u'放送大学１'),
        (11,u'その他'),
        )
    WAVE_CHOICES = (
        (1,u'DFS00400'),
        (2,u'DFS00408'),
        (4,u'DFS00410'),
        (5,u'DFS00428'),
        (6,u'DFS00418'),
        (7,u'DFS00430'),
        (8,u'DFS00420'),
        (9,u'DFS05C38'),
        (10,u'DFS00440'),
        (11,u'UNKNOWN'),
        )

    title = models.ForeignKey(Title)
#    title = models.CharField(max_length = 50 )
    program_id = models.IntegerField()
    waves = models.IntegerField(choices= WAVE_CHOICES)
#    waves = models.ForeignKey(Waves)
    station = models.IntegerField(choices= STATION_CHOICES)
#    station = models.ForeignKey(Station)
#    wave = models.CharField(max_length = 10 )
#    station = models.CharField(max_length = 10 )
    start = models.DateTimeField()
    end = models.DateTimeField()
    gen_1 = models.IntegerField(choices= GENRE_CHOICES)
    sgn_1 = models.IntegerField(choices= SUBGEN_CHOICES)
    gen_2 = models.IntegerField(choices= GENRE_CHOICES)
    sgn_2 = models.IntegerField(choices= SUBGEN_CHOICES)
    comments = models.ForeignKey(Comments)
#    comments = models.CharField(max_length = 80 )

    def __unicode__(self):
        return self.title.name
