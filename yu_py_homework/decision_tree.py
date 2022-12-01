'''
Version: 1.0
Author: xiawei
Date: 2022-11-21 19:31:20
LastEditors: xiawei
LastEditTime: 2022-11-25 20:33:13
Description: 采用决策树算法，找到优惠券使用人群的特点和规律

1. 如何理解决策树的生长过程是对变量空间的反复划分过程？
将有相似输出的变量归类，递归进行以此目的的划分,形式就是变量空间的反复划分
2. 决策树生长的基本原则
没有出现过拟合
3.请采用决策树算法，找到优惠券使用人群的特点和规律:
  由模型得知：性别是决定是否使用优惠券的决定性因素，女生比男生更容易使用。使用券人数多余未使用人数
'''
"""from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
import sklearn
from sklearn.metrics import accuracy_score
from sklearn import tree
print(sklearn.__version__)
current_directory = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(current_directory+'./优惠券核销数据.csv')
# data = data.replace(0, np.NAN)
print(data.head())

X = data.loc[:, ['Class', 'Sex', 'Age', 'AvgSpending']]
y = data.loc[:, 'Accepted']
dc_tree = tree.DecisionTreeClassifier(
    criterion='entropy', min_samples_leaf=1, max_depth=20)
dc_tree.fit(X, y)
score = accuracy_score(y, dc_tree.predict(X))
print('dc_tree_score', score)
fig = plt.figure(figsize=(10, 10))
tree.plot_tree(dc_tree, filled='True', feature_names=[
    'Class', 'Sex', 'Age', 'AvgSpending'], class_names=['0', '1'], fontsize=5)
# plt.savefig(current_directory+'./1.png', dpi=4000)
plt.show()
"""
le = LabelEncoder()
data["SexC"] = le.fit(data["Sex"]).transform(data["Sex"])  # 原本是女1，男2
# 液奶品类（Class:低端1、中档2、高端3），是否使用优惠券（Accepted：使用1、未使用0）
data["ClassC"] = le.fit(data["Class"]).transform(data["Class"])
data["AvgSpendingC"] = le.fit(data["AvgSpending"]).transform(
    data["AvgSpending"])  # 平均花费
data["AgeC"] = le.fit(data["Age"]).transform(data["Age"])  # age1中青年，中老年2
data.head()

X = data[['AgeC', 'SexC', 'ClassC', 'AvgSpendingC']]
Y = data['Accepted']  # 分别以年龄，性别，购买奶类型，平均花费为自变量，是否使用优惠券为因变量进行拟合
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, train_size=0.72, random_state=123)
trainErr = []
testErr = []
K = np.arange(2, 30)  # 分别取树深度，以便选取更好的的拟合效果
for k in K:
    modelDTC = tree.DecisionTreeClassifier(max_depth=k, random_state=123)
    modelDTC.fit(X_train, Y_train)
    trainErr.append(1-modelDTC.score(X_train, Y_train))
    testErr.append(1-modelDTC.score(X_test, Y_test))
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
axes[0].grid(True, linestyle='-.')  # 设定表格1，2输出样式
axes[0].plot(np.arange(2, 30), trainErr,
             label="训练误差", marker='*', linestyle='-')
axes[0].plot(np.arange(2, 30), testErr, label="测试误差",
             marker='*', linestyle='-.')

axes[0].set_xlabel("树深度")
axes[0].set_ylabel("误差")
axes[0].set_title('树深度和误差')
axes[0].legend()
bestK = K[testErr.index(np.min(testErr))]
modelDTC = tree.DecisionTreeClassifier(max_depth=bestK, random_state=123)
modelDTC.fit(X_train, Y_train)
axes[1].bar(np.arange(4), modelDTC.feature_importances_)
axes[1].set_title('输入变量重要性')
axes[1].set_xlabel('输入变量')
axes[1].set_xticks(np.arange(4))
axes[1].set_xticklabels(['年龄', '性别', '类型', '平均消费'])
plt.show()
print("模型的评价:\n", classification_report(
    Y, modelDTC.predict(X)))  # 显示决策树主要分类指标的文本报告
print(tree.export_text(modelDTC))  # 输出决策树模型
