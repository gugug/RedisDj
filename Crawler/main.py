# coding=utf-8
import datetime

from Crawler.down_username import *
from MoblieWeibo import MoblieWeibo

__author__ = 'gu'


def count_time():
    """
    显示时间
    :return:
    """
    now = datetime.datetime.now()
    other_style_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print other_style_time
    return other_style_time


account = {1: ('gwcrawler1@126.com', '321456'),
           3: ('shuqunkeji@sina.com', 'shujuwajue'),
           5: ('zgryejmd@sina.cn', 'tttt5555'), 6: ('nowccqpq@sina.cn', 'tttt5555'),
           7: ('odlmyfbw@sina.cn', 'tttt5555'), 8: ('ajjqbwkm@sina.cn', 'tttt5555'),
           10: ('coiarurd@sina.cn', 'tttt5555'),17:('zcsicrod@sina.cn', 'tttt5555'),
           13: ('cjmnkaok@sina.cn', 'tttt5555')

           }
# 2: ('iydt30@mailnesia.com', 'pp9999'), 4: ('gdufsiiip@sina.com', 'shujuwajue'), 11: ('oaax1n@mailnesia.com', 'pp9999')
# 12: ('nrrfdzpc@sina.cn', 'tttt5555'), 14: ('fwg4cp@mailnesia.com', 'pp9999'),
# 15: ('gxyb5w@mailnesia.com', 'pp9999'), 16: ('agfpuo@mailnesia.com', 'pp9999')

MoblieWeibo().login(account[1][0], account[1][1])
start_time = datetime.datetime.now()
# 主机会put, 其他机器只管down就好
main_down_stats(5, 1) # 分机数目, 机器编号
print '总共用时间为： ', datetime.datetime.now() - start_time
