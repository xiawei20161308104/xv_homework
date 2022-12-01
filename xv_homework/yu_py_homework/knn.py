'''
Version: 1.0
Author: xiawei
Date: 2022-11-23 19:26:33
LastEditors: xiawei
LastEditTime: 2022-11-23 21:23:17
Description: Python机器学习最后大作业
2. K-最近邻域算法（K-NearestNeighbor,KNN）。实现KNN算法（K值和距离度量可自行指定）,创建一个训练集以及一个测试样本，在该训练集上训练KNN算法，并预测该测试样本。
'''
# KNN具体实现
import csv  # 这读取数据用的。
import random  # 进行随机变量的运算的过程的。
import math
import operator  #
from IPython import embed

# 首先是要把用的数据集给装载进来的。
# split是可以来把原始的数据集，来分为两个部分，一部分是trianSet,一部分是testset
# split把原始数据集分为train和test数据集的过程的。


def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)  # 这里是来把数据转换成为一行一行，所对应的数据
        # 然后这里是来把数据集，列表的方式进行输出的['1 5.1 3.5 1.4 0.2 "setosa"']
        dataset = list(lines)
        # 这里总共是对应的150行数据的
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:  # 这里是来对应的随机量是小于这个split的值的时候，那么我们就认为把
                # 这一行数据给加入到trainingSet数据集中，反之则是加入到testSet所对应的数据集中的。
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

# 这里是来传入两个实例，以及他所对应的维度。
# 传入是相应的测试实例，和相应训练的实例，特征的长度是对应的为4


def euclideanDistance(intstance1, instance2, length):
    distance = 0
    for x in range(length):
        # 然后是对应的每个维度相减后，所对应的平方值。最后是把这几个维度来进行求和
        distance += pow((intstance1[x]-instance2[x]), 2)
        return math.sqrt(distance)  # 开方值的过程的。这样就是来最后是返回相应的开方值的过程的。

 # 这个是来返回测试实例中的，最近的k实例在训练集中的过程的
 # 是来对应的训练数据集，和相应的测试数据集，和对应的相应的k近邻


def getNeighbors(trainingSet, testInstance, k):
    distances = []  # 定义一个容器，来装所有距离的过程的。
    length = len(testInstance)-1  # 测试的维度
    for x in range(len(trainingSet)):
        dist = euclideanDistance(
            testInstance, trainingSet[x], length)  # 然后是来计算出相应的欧式距离
        # ([5.1, 3.5, 1.4, 0.2, 'Iris-setosa'], 0.09999999999999964)是来得到相应的训练集的特征
        # 得到与测试样列之间，所对应的距离的。
        distances.append((trainingSet[x], dist))  # 每一次算出的距离加入，
    distances.sort(key=operator.itemgetter(1))  # 对距离进行排序
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])  # 找出相应的最小的k个作为相应的邻居的
    return neighbors

# 统计每一个分类的投票的多少，投票得到最多的模块，的分类


def getResponse(neighbors):
    classVotes = {}  # 根据这k实例来进行投票法则的
    for x in range(len(neighbors)):
        response = neighbors[x][-1]  # 这里来返回，最后所对应的种类标签的。
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1  # 首先是来把标签进行加入后，
    sortedVotes = sorted(classVotes.items(),
                         key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]  # 投票后，这样来得到花，所对应的类别的过程的。

# 预测的所有值，的准确率是有多少的过程的。


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:  # -1是取最后一个值。如果是预测的结果与测试结果是相同的。
            correct += 1  # 那么就是correct+1

    return (correct/float(len(testSet))) * 100.0  # 这样最后就是可以得到相应的准确性了


def main():
    trainingSet = []  # 这里是来对应的相应的训练数据集
    testSet = []  # 这里是来对应相应的测试数据集的过程的。
    split = 0.67  # 按照两份和1份的方式来对相应的数据集，进行划分的过程的。
    # r当成是原始的字符串进行对待，忽略出特殊字符的过程的。
    loadDataset(r'D:\Pratice Code\MLeaning\data\Iris数据集\1.txt',
                split, trainingSet, testSet)
    print("train set:" + repr(len(trainingSet)))
    print('Test set:' + repr(len(testSet)))
    # generate predictions是来表示生成相应的预测值的过程的
    predictions = []
    k = 3  # 其中是k是等于3来表示相应的分类的过程的。
    for x in range(len(testSet)):
        # 然后是来首先是对每一个测试数据集进行输入
        # 这里是来返回每个实例对应的最近的k个实例的
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)  # 归类的值，
        predictions.append(result)  # 得到相应的全部的预测结果。
        # >predicted='Iris-setosa',actual='Iris-setosa'
        print('>predicted='+repr(result)+',actual='+repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:'+repr(accuracy)+'%')


if __name__ == '__main__':
    print('')
