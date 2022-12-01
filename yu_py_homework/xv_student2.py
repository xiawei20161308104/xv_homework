'''
Version: 1.0
Author: xiawei
Date: 2022-10-20 10:06:27
LastEditors: xiawei
LastEditTime: 2022-10-20 19:49:33
Description: python第一次作业
1. 有60名学生的两门课程成绩的数据文件（ReportCard1.txt和ReportCard2.txt），分别记录着学生的学号、性别以及不同课程的成绩。请将数据读入Pandas数据框，并做如下预处理和基本分析：
1）将两个数据文件按学号合并为一个数据文件，得到包含所有课程成绩的数据文件。
2）计算每位同学的各门课程的总成绩和平均成绩。
3）将数据按总成绩的降序排序。
4）按性别分别计算各门课程的评平均成绩。
5）按优、良、中、及格和不及格，对平均成绩进行分组。
6）按性别统计优、良、中、及格和不及格的人数。
7）生成性别的虚拟自变量
2. 学生成绩数据的图形化展示。
对包含所有课程成绩的数据文件，做如下图形化展示：
1）绘制总成绩的直方图。
2）绘制平均成绩的优、良、中、及格和不及格的饼图。
3）绘制总成绩和数学（math）成绩的散点图。
'''
from cv2 import merge
from logger1 import logger as log
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import os


# 获取当前路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# 读取文件，注意分隔符
# 展示每个类别总样本
data1 = pd.read_csv(
    current_directory+'./ReportCard1.txt', sep='\t', na_values=['NAN', 'NA'])
log.info(data1.count())
# 展示每个类别缺失值个数
log.info(data1.isnull().sum())
# 发现样本有缺失值。将缺失值人工转为0
data1 = data1.fillna(0)
log.info('data1')
log.info(data1)
# data2做相同处理
data2 = pd.read_csv(
    current_directory+'./ReportCard2.txt', sep='\t', na_values=['NAN', 'NA'])
# 发现data2没有缺失值
# data2 = data2.fillna(0)

data_merge = pd.merge(data1, data2, how="outer", on="xh", sort=False)
log.info('data_merge')
log.info(data_merge)
log.info(data_merge.isnull().sum())
mean_col = data_merge[['poli', 'chi', 'math',
                       'fore', 'phy', 'che', 'geo', 'his']].mean(axis=1)
type(mean_col)
sum_col = data_merge[['poli', 'chi', 'math',
                      'fore', 'phy', 'che', 'geo', 'his']].sum(axis=1)
log.info(mean_col)
log.info(sum_col)
sum_col = pd.DataFrame(sum_col)
mean_col = pd.DataFrame(mean_col)
# data里加上总成绩列
data_merge['sum_score'] = sum_col
data_merge['mean_score'] = mean_col
log.info(data_merge)
data_dsc = data_merge.sort_values('sum_score', ascending=False)
log.info(data_dsc)
data_mean_by_sex = data_merge.groupby('sex').mean()
log.info(data_mean_by_sex)

# 按照优、良、中、及格、不及格对平均成绩进行分组
data_merge['degree'] = data_merge['mean_score']. \
    apply(lambda x: "优" if x > 90 else
          "良" if x > 80 else
          "中" if x > 70 else
          "及格" if x > 60 else "不及格")
log.info(data_merge)

count = data_merge.groupby('sex')['degree'].value_counts()
log.info(count)

# 绘图
# 总成绩直方图
sum_score = data_merge['sum_score'].values
fig0 = plt.figure(figsize=(10, 5))
plt.hist(sum_score, label="sum_score_hist")
plt.title('总成绩直方图')
plt.show()


# 绘制平均成绩的优、良、中、及格、不及格饼图
fig1 = plt.figure(figsize=(10, 10))
plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False

plt.pie(data_merge['degree'].value_counts(),
        labels=['良', '中', '及格', '不及格'],
        autopct='%.2f%%')
plt.title('优、良、中、及格、不及格饼图')
plt.show()

# 总成绩和数学成绩散点图
fig1 = plt.figure(figsize=(10, 10))
plt.scatter(data_merge['sum_score'].values, data_merge['math'].values)
plt.title('总成绩和数学成绩散点图')
plt.show()
