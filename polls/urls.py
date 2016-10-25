# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-10-24 12:13:46
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-10-25 13:49:24

from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'polls'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]