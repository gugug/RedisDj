# coding=utf-8
from django.db import models
from django.contrib import admin

class Headhunter(models.Model):  # 猎头信息表
    user_id = models.CharField('用户id', max_length=20, primary_key=True)
    user_name = models.CharField('昵称', max_length=20)
    gender = models.CharField('性别', max_length=6, default='未知')
    birth = models.DateField('生日')
    vip_state = models.CharField('认证信息', max_length=30)
    location = models.CharField('地区', max_length=10)
    profile = models.TextField('简介', max_length=300)
    tag = models.CharField('标签', max_length=200)
    fans_num = models.IntegerField('粉丝数', default=0)
    follow_num = models.IntegerField('关注数', default=0)
    blog_num = models.IntegerField('微博数', default=0)

    def __unicode__(self):
        return u'%s %s %s' % (self.user_name, self.vip_state, self.location)

    class Meta:
        db_table = 'headhunter'

class HeadhunterAdmin(admin.ModelAdmin):
    search_fields = ('user_id', 'user_name', 'vip_state', 'location')
