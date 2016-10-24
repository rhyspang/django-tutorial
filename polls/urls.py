# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-10-24 12:13:46
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-10-24 18:38:50

from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'polls'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.result, name='result'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]