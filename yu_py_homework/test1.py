'''
Author: xiawei
Date: 2022-10-20 10:03:09
LastEditors: xiawei
LastEditTime: 2022-10-20 16:06:45
description: 冉同学编写的python第一个作业
'''
import pandas as pd
import matplotlib.pylab as plt
import matplotlib as mpl
import os
# 获取当前路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

df_student1 = pd.read_table(current_directory+'/ReportCard1.txt')
df_student2 = pd.read_table(current_directory+'/ReportCard2.txt')
# df_student1 = pd.read_table(current_directory+'/ReportCard1.txt')
# df_student2 = pd.read_table(current_directory+'/ReportCard2.txt')

# 合并两个表为一个表
df_student = df_student1.merge(
    df_student2, on='xh', how='outer', validate='1:1')
# print(df_student)

df_student = df_student.set_index('xh')

# 处理缺省值
df_student = df_student.fillna(0)
# print(df_student)

# 计算总成绩
df_student['TotalScore'] = df_student['poli'] + df_student['chi'] + df_student['math'] + \
    df_student['fore'] + df_student['phy'] + df_student['che'] + \
    df_student['geo'] + df_student['his']
# 计算平均成绩
df_student['MeanScore'] = df_student['TotalScore'] / 8

# 按总成绩降序
df_student = df_student.sort_values('TotalScore', ascending=False)
# print(df_student)

# 按性别计算各门课程平均成绩
print('poli')
print(df_student.groupby('sex')['poli'].mean())
print('chi')
print(df_student.groupby('sex')['chi'].mean())
print('math')
print(df_student.groupby('sex')['math'].mean())
print('fore')
print(df_student.groupby('sex')['fore'].mean())
print('phy')
print(df_student.groupby('sex')['phy'].mean())
print('che')
print(df_student.groupby('sex')['che'].mean())
print('geo')
print(df_student.groupby('sex')['geo'].mean())
print('his')
print(df_student.groupby('sex')['his'].mean())

# 按照优、良、中、及格、不及格对平均成绩进行分组
df_student['Category'] = df_student['MeanScore']. \
    apply(lambda x: "优" if x > 90 else
          "良" if x > 80 else
          "中" if x > 70 else
          "及格" if x > 60 else "不及格")

# print(df_student)

# 按照性别统计优、良、中、及格、不及格的人数
print(df_student.groupby('sex')['Category'].value_counts())

# 绘图
# 总成绩直方图
# totalscore = df_student['TotalScore'].values
# plt.hist(totalscore, label="TotalScoreHist")
# plt.legend()
# plt.show()


# 绘制平均成绩的优、良、中、及格、不及格饼图
# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# mpl.rcParams["axes.unicode_minus"] = False
#
# plt.pie(df_student['Category'].value_counts(),
#         labels=['良', '中', '及格', '不及格'],
#         autopct='%.2f%%')
# plt.show()

# 总成绩和数学成绩散点图
plt.scatter(df_student['TotalScore'].values, df_student['math'].values)
plt.show()
