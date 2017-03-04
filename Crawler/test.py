# coding=utf-8

__author__ = 'gu'

# print "test"
# redis_key = ''
# db = redis.Redis(host='192.168.235.51', port=6379, db=0)
# print db.exists('event:孙杨不哭')
# kes = db.keys("event*")
# for i in kes:
# #     print i
# s = [1,2,3,4,5,6,7]
#
# for i in s[0:3]:
#     print i


import time
time.strftime('%Y%m%d')
# //获取了当前时间的年月日

# 获取昨天的时间datetime

import datetime
# now_time = datetime.datetime.now()
# print now_time
# yes_time = now_time + datetime.timedelta(days=-1)
# yes_time_nyr = yes_time.strftime('%Y%m%d')    #//格式化输出
#
# print yes_time_nyr


# 1.python求时间差不能使用time()模块，eg：
# t1 = time.ctime()
# time.sleep(3)
# t2 = time.ctime()
# t = t2 - t1    ###会报错，不能相减


# 2.需要使用datetime模块，datetime模块比time模块更能更强。
# d1 = datetime.datetime.now()
# time.sleep(3)
# d2 = datetime.datetime.now()
#
# d = d2 - d1    ### 产生的是 datetime.timedelta 对象
# print d

# d.days 天
# d.max 最大
# d.microseconds 微秒
# d.min 最小
# d.resolution
# d.seconds 秒
#
# 注： d1, d2 还可以格式化成正常的日期时间。
# e.g:
# t_now = str(d1)  ### t_now = '2012-02-17 12:49:04.828000'  精确到毫秒
# t_now[:19]  ## 秒级别 '2012-02-17 12:49:04'
# t_now[:10]  ## 日期级别 '2012-02-17'



d1 = datetime.datetime.now()
d2 = datetime.datetime(d1.year,d1.month,d1.day,6,6,0)
d3 = d2 + datetime.timedelta(days=1)
print d1
print d3
wait_time = d3-d1
print wait_time.seconds

# print wait_time.hour
# print wait_time.minute
# print wait_time.second