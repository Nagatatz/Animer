#from django.conf.urls import patterns, include, url
from django.conf.urls import * #for auth

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       url(r'^iepg/$','iepg.views.index'),
                       url(r'^iepg/id/(?P<id>\d+)/$','iepg.views.id'),
                       url(r'^iepg/sta/(?P<station>\d+)/$','iepg.views.sta'),
                       url(r'^iepg/g1/(?P<gen_1>\d+)/$','iepg.views.g1'),
                       url(r'^iepg/sg1/(?P<sgn_1>\d+)/$','iepg.views.sg1'),
                       url(r'^admin/', include(admin.site.urls)),
                       #add for login
                       url(r'^make/$', 'iepg.views.make'),
                       url(r'^enter/$', 'iepg.views.enter'),
                       url(r'^out/$', 'iepg.views.out'),
                       url(r'^mypage/$', 'iepg.views.mypage'),
                       url(r'^login/$', 'iepg.views.idx'),
                       url(r'^add/$', 'iepg.views.add'),
                       #url(r'^logout/$','iepg.views.logout_view'),
                       )

