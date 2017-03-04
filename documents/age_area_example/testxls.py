# coding=utf-8
from datetime import datetime
from xlwt import *
import xlwt
import os

__author__ = 'gu'

# w =Workbook()
#
# ws = w.add_sheet('xlwtwas here')
# w.save('mini.xls')


# def write_xls(areas):
#         """
#         把地区信息写入xls文件
#         :param path: 生成xls的上级目录
#         :return: xls文件路径
#         """
#         xls = xlwt.Workbook('utf-8')
#         # table = xls.add_sheet('age_distribution',True)
#         # sorted_dict = sorted(self.age.iteritems())  # [(key,value),()]
#         # for row in range(0,len(self.age)):
#         #     table.write(row,0,sorted_dict[row][0])
#         #     table.write(row,1,sorted_dict[row][1])
#         table = xls.add_sheet('map', True)
#         sorted_dict = sorted(areas.iteritems())  # [(key,value),()]
#         for row in range(0, len(areas)):
#             table.write(row, 0, sorted_dict[row][0])
#             table.write(row, 1, sorted_dict[row][1])
#         xls_file = os.path.join('map.xls')
#         xls.save(xls_file)
#         return xls_file




def write_data_to_excel(file_name, areas):
    result = [(1,0),(2,3),(4,6)]
    # 将sql作为参数传递调用get_data并将结果赋值给result,(result为一个嵌套元组)
    # 实例化一个Workbook()对象(即excel文件)
    wbk = xlwt.Workbook()
    # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    sheet = wbk.add_sheet('map', cell_overwrite_ok=True)
    # 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)
    today = datetime.today()
    # 将获取到的datetime对象仅取日期如：2016-8-9
    today_date = datetime.date(today)
    # 遍历result中的没个元素。
    for i in xrange(len(result)):
        #对result的每个子元素作遍历，
        for j in xrange(len(result[i])):
            #将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i,j,result[i][j])
    # 以传递的name+当前日期作为excel名称保存。
    wbk.save(name+str(today_date)+'.xls')

# 如果该文件不是被import,则执行下面代码。
if __name__ == '__main__':
    #定义一个字典，key为对应的数据类型也用作excel命名，value为查询语句
    db= 'test'
    # 遍历字典每个元素的key和value。
        # 用字典的每个key和value调用write_data_to_excel函数。
    write_data_to_excel(db)