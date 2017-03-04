# coding=utf-8
__author__ = 'gu'

# q = RedisQueue('yuqing')  # 键的名字
# q.put('hello world1')  # 加一个进去
# q.get()   # 取出第一个值并且移出
# print q.get()        st = StatsAll()

from Crawler.stats_all import *
st = StatsAll()
st.do_all('s','0000-00','f')
st.print_all()  # 打印统计结果
