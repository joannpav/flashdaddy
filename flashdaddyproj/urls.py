from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flashdaddyproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'flashdaddy.views.home', name='home'),
	url(r'^createCard/', 'flashdaddy.views.createCard', name='createCard'),
	url(r'^ocr/', 'flashdaddy.views.ocr', name='ocr'),

    #url(r'^admin/', include(admin.site.urls)),
)
