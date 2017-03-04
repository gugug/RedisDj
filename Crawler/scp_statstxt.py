# coding=utf-8

import os
from time import sleep

import re

__author__ = 'gu'

salve_master = {'gu': '192.*.*.*','fen':'192.*.*.*'}

def scp_to_master(file_name, YOURID):
    """
    上传对应文件夹下的txt到master
    :param file_name: txt所在的文件夹的目录
    :param YOURID: slave的编号
    :return:
    """
    # file_name = '/home/gu/PycharmProjects/RedisDj/documents/topic/孙杨'
    topic = re.split('/',file_name)
    stats_txt = file_name + '/stats'+str(YOURID)+'.txt'
    is_exists = os.path.exists(stats_txt)
    if not is_exists:
        pass
    else:
        print '上传....'
        scp_chmod = 'scp -p ' + stats_txt + ' username@192.*.*.*:/home/username/PycharmProjects/RedisDj/documents/topic/'+topic[-1]
        is_succeed = os.system(scp_chmod)
        if is_succeed:
            print "休眠5s, 再次尝试上传master"
            sleep(5)
            scp_to_master(file_name, YOURID)
        else:
            print "上传成功", scp_chmod


        # rm_chmod = 'rm -r ' + file_name
        # os.system(rm_chmod)



# scp_to_master('/home/fen/WorkPlace/RedisDj/documents/topic/2016里约奥运会',1)

