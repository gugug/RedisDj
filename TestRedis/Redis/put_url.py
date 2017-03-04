# coding=utf-8
import random

"""
先用一段代码将URL放进redis queue中
"""

from bs4 import BeautifulSoup
import urllib2
from Queue import Queue
from Crawler import RedisQueue

__author__ = 'gu'

queue = Queue()
redis = RedisQueue('jandan') # 键的名字 queue:jandan3

def user_agent(url):
    """
    代理
    :param url:
    :return:
    """
    req_header = {'User-Agent': 'Mozilla/' + str(
            float(int(random.uniform(1, 6)))) + '(X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/' + str(
            float(int(random.uniform(29, 36))))}
    req_timeout = 20
    req = urllib2.Request(url, None, req_header)
    page = urllib2.urlopen(req, None, req_timeout)
    html = page
    return html

def next_page():

    base_url = 'http://jandan.net/ooxx/page-1006#comments'

    for i in range(5):
        html = user_agent(base_url).read()
        soup = BeautifulSoup(html)

        next_url = soup.find('a', {'class': 'next-comment-page', 'title': 'Newer Comments'}).get('href')

        yield base_url  # 先return 然后next
        base_url = next_url


for page in next_page():
    print page
    queue.put(page)  # 把页数放进队列
print 'There are %d pages' % queue.qsize()


while not queue.empty():  # 如果队列不空

    page_url = queue.get()  # 取第一个然后移出
    print page_url
    html = user_agent(page_url).read()

    soup = BeautifulSoup(html)

    img_urls = soup.find_all(['img'])

    for myimg in img_urls:
        Jpgurl = myimg.get('src')
        redis.put(Jpgurl)

print 'There are %d pictures' % redis.qsize()


