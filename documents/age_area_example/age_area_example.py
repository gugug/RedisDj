# coding=utf-8
import os
import json
import xlrd
import xlwt


def write_xls(path, areas):
    """
    把地区信息写入xls文件
    :param path: 生成xls的上级目录
    :return: xls文件路径
    """
    xls = xlwt.Workbook('utf-8')
    # table = xls.add_sheet('age_distribution',True)
    # sorted_dict = sorted(self.age.iteritems())  # [(key,value),()]
    # for row in range(0,len(self.age)):
    #     table.write(row,0,sorted_dict[row][0])
    #     table.write(row,1,sorted_dict[row][1])
    table = xls.add_sheet('map', True)
    sorted_dict = sorted(areas.iteritems())  # [(key,value),()]
    for row in range(0, len(areas)):
        table.write(row, 0, sorted_dict[row][0])
        table.write(row, 1, sorted_dict[row][1])
    xls_file = os.path.join(path, 'map.xls')
    xls.save(xls_file)
    return xls_file



def dump_json():
    """
    生成age distribution ,map的json文件
    :param xls_file: xls文件的路径
    :return:
    """

    age = [1,2,3,4]
    age_dict = {}
    age_dict.setdefault('ageDistribution', age)
    age_json = json.dumps(age_dict, separators=(',', ':'))
    age_file = open(os.path.join('age_distribution.json'), 'w+')
    age_file.writelines(age_json)
    age_file.close()

    # map_list = []
    # xls = xlrd.open_workbook(xls_file)
    # table = xls.sheet_by_index(0)
    # name_list = table.col_values(0, 0)
    # value_list = table.col_values(1, 0)
    # for i in range(0, len(name_list)):
    #     map_dict = {'name': name_list[i], 'value': value_list[i]}
    #     map_list.append(map_dict)
    # data_dict = {'map': map_list}
    # map_json = json.dumps(data_dict, separators=(',', ':'))
    # map_file = open(os.path.join('map111.json'), 'w+')
    # map_file.writelines(map_json)
    # map_file.close()
    # print 'finish writing age and map json'
    # return True


dump_json()