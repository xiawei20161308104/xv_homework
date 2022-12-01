'''
Version: 1.0
Author: xiawei
Date: 2022-11-21 09:27:46
LastEditors: xiawei
LastEditTime: 2022-11-21 11:05:50
Description: 采用Logistic回归模型和朴素贝叶斯分类器，对是否使用奶制品优惠券进行二分类预测。


问题一：在假定输入变量对于给定输出变量条件独立下，该分类器称为朴素贝叶斯分类器
'''
from sklearn.metrics import classification_report
import sklearn.linear_model as LM
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
from sklearn.naive_bayes import GaussianNB

current_directory = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(current_directory+'./优惠券核销数据.csv')
# data = data.replace(0, np.NAN)
print(data.head())

X = data.loc[:, ['Class', 'Sex', 'Age', 'AvgSpending']]
Y = data.loc[:, 'Accepted']
Y = np.array(Y).reshape(-1, 1)
modelNB = GaussianNB()
modelNB.fit(X, Y)

modelLR = LM.LogisticRegression()
modelLR.fit(X, Y)

print('评价模型结果：\n', classification_report(Y, modelNB.predict(X)))
