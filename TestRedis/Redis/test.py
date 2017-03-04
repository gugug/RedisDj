# coding=utf-8
import re

__author__ = 'gu'

# def next_page():
#
#     base_url = 'http://jandan.net/ooxx/page-1006#comments'
#
#     for i in range(3):
#         print i
#         print "html>>>>>>>>>>>>>>>>."
#
#         next_url = "http://www.baidu.com"+str(i)
#
#         yield base_url  # return 然后接着next()
#         base_url = next_url
#
#
# for page in next_page():
#     print page
#
# for i in range(3):
#     print i
#
#
# htmlPage = """
# """

# soup = BeautifulSoup(htmlPage)
#
# img_urls = soup.find_all(['img'])
# print img_urls
# for myimg in img_urls:
#     print "my", myimg
#     Jpgurl = myimg.get('src')
#     print 'Jpgurl', Jpgurl

# down_url = 'www.baidu.com'
# with open('/home/gu/PycharmProjects/TestRedis/Redis'+'/'+down_url[-11:],'wb')as code:
#     code.write('asd')
#     print 'dd'
# r = RedisQueue('username')
# r.put('Miolhnc')
# r.get()
homepage = """<span class="ctt">流沙-ff&nbsp;女/北京    &nbsp;    <a href="/attention/add?uid=1881380547&amp;rl=0&amp;st=4be8da">加关注</a></span><br /><span class="ctt" style="word-break:break-all; width:50px;"></span><br /><a href="/im/chat?uid=1881380547&amp;rl=0">私信
"""
def get_name():
    """
    首页上取到用户名
    :return: 用户名(str)
    """
    name_pattern = re.compile('<span class="ctt">(.*?)<.*?uid=.*?>私信')
    name = name_pattern.findall(homepage)
    label_pattern = re.compile('&nbsp.*?$')
    name = re.sub(label_pattern,'',name[0])
    print name
    return name
#
#
get_name()
#
# data_dir = os.path.join(BASE_DIR, 'documents', 'data/')
# data_file = open(data_dir + 'uid=' + get_name() + '.txt', 'w+')
# data_file.close()