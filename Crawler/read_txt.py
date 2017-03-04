from Queue import Queue
from RedisDj.settings import *

__author__ = 'gu'

# queue = Queue()
# def read_txt(file_name):
#     participants_txt = os.path.join(BASE_DIR, 'documents', 'topic', file_name)
#     txt = open(participants_txt, 'r')
#     name_list = []
#     words = txt.readlines()
#     for i in range(len(words)):
#         words[i] = words[i].replace('\n','')
#         print words[i]
#         name_list.append(words[i])
#         queue.put(words[i])
#     return name_list

# read_txt('participants.txt')