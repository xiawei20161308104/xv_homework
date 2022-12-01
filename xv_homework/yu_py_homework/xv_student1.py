
import pandas as pd
import numpy as np
import os

'''# 获取当前路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# 将txt中数据按行读取到data里面作为元数据
data1 = open(current_directory+'/ReportCard1.txt',
             encoding='utf-8').readlines()
data2 = open(current_directory+'/ReportCard2.txt',
             encoding='utf-8').readlines()
# print(type(data2))

# 定义各属性数据存储列表
file1_xh = []
file1_sex = []
file1_poli = []
file1_chi = []
file1_math = []

file2_xh = []
file2_fore = []
file2_phy = []
file2_che = []
file2_geo = []
file2_his = []
# 遍历data1
for message in data1:
    temp_list = message.split()
    # 将txt文件中的第一行 也就是file_list1 列表的第一项
    # 用split方法操作 以空格为分隔符 分成两部分继续放到temp_list列表里
    file1_xh.append(str(temp_list[0]))
    file1_sex.append(str(temp_list[1]))
    file1_poli.append(str(temp_list[2]))
    file1_chi.append(str(temp_list[3]))
    file1_math.append(str(temp_list[4]))

# 同样处理data2
for message in data2:
    temp_list = message.split()
    file2_xh.append(str(temp_list[0]))
    file2_fore.append(str(temp_list[1]))
    file2_phy.append(str(temp_list[2]))
    file2_che.append(str(temp_list[3]))
    file2_geo.append(str(temp_list[4]))
    file2_his.append(str(temp_list[4]))

file_list3 = []
for i in range(len(file1_xh)):
    s = ''
    if file1_xh[i] in file2_xh:
        j = file2_xh.index(file1_xh[i])  # 列表index方法 查找括号内对象 返回值为索引位置

        s = '\t'.join([file1_xh[i], file1_sex[i], file1_poli[i], file1_chi[i], file1_math[i],
                       file2_xh[j], file2_fore[j], file2_phy[j], file2_che[j], file2_geo[j], file2_his[j]])
        # 字符串join方法连接三个属性,之间以(\t 制表位)隔开
        s += '\n'
    file_list3.append(s)
    print(file_list3)
'''
m,n=5,4
m,n=n,n+m
print(m)
print(n)