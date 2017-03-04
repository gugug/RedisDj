# coding=utf-8
from redisyq.views import *
from django.conf.urls import url

__author__ = 'gu'

urlpatterns=[

    url(r'^index/$',index,name='index'),


]