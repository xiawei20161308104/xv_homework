'''
Version: 1.0
Author: xiawei
Date: 2022-11-23 19:26:33
LastEditors: xiawei
LastEditTime: 2022-11-23 21:19:46
Description: Python机器学习最后大作业
1.一元线性回归。利用y=kx+b+ε,随机生成含100个数据的数据集S={(x1,y1),...,(x100,y100)},这里常数k,b可自由指定,ε为服从某个指定分布（如标准正态分布、均匀分布等）的随机变量。利用数据集S,通过梯度下降法最小化损失函数loss=100∑i=1(yi−ˆyi)2（这里ˆyi=ˆkxi+ˆb）迭代求解ˆk和ˆb,从而拟合直线y=ˆkx+ˆb,并在一张图中画出数据集S的散点图和y=ˆkx+ˆb的直线图。特别说明:必须按题目要求自己实现一元线性回归代码,不能调用第三方已实现好的线性回归算法.
'''
import numpy as np
from matplotlib import pylab as plt
# 生成训练集x
x = np.ones((100, 1))
for i in range(100):
    x[i, 0] = np.random.random()
print(x)

# 生成训练集y
y = np.zeros((100, 1))
for k in range(100):
    random1 = np.random.random()
    y[k, 0] = 2 * x[k, 0]+3+random1
print(y)


def fit(x, y):
    if len(x) != len(y):
        return
    numerator = 0.0
    denominator = 0.0
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += np.square((x[i]-x_mean))
    print('numerator:', numerator, 'denominator:', denominator)
    b0 = numerator/denominator
    b1 = y_mean - b0*x_mean
    return b0, b1


def predit(x, b0, b1):
    return b0*x + b1


k, b = fit(x, y)
print('Line is:y = %2.0fx + %2.0f' % (k, b))
plt.scatter(x, y, cmap=plt.cm.Paired)
plt.plot(x, k*x+b, 'r')
plt.show()
