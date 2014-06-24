# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.login.views',
    url(r'^$', 'index', name='login_index'),
    url(r'^account/$', 'account', name='login_account'),
    url(r'^account/callback/$', 'callback', name='login_callback'),
)
