# coding=utf-8
import random

__author__ = 'gu'
import urllib2

from Crawler import RedisQueue

redis = RedisQueue('jandan')

def user_agent(url):
    req_header = {'User-Agent': 'Mozilla/' + str(
        float(int(random.uniform(1, 6)))) + '(X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/' + str(
        float(int(random.uniform(29, 36))))}
    req_timeout = 20

    req = urllib2.Request(url, None, req_header)

    page = urllib2.urlopen(req, None, req_timeout)

    html = page
    return html


while not redis.empty():
    try:
        down_url = redis.get()
        data = user_agent(down_url).read()
        with open('BASE_DIR/TestRedis/Redis/result'+'/'+down_url[-11:],'wb')as code:
            code.write(data)
        print down_url
    except:
        pass
