# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-10-24 12:13:46
# @Last Modified by:   rhys
# @Last Modified time: 2016-10-24 12:54:06

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]