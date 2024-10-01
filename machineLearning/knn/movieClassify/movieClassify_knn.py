import os

import numpy as np
import operator

"""
函数说明：创建数据集
parameters:
Returns:
group -数据集
labels- 分类标签
"""


# 创建数据
def createDataSet():
    # 四组二维特征,[1,101]表示打斗画面有1个，接吻画面有101个，一共4组样本
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    print("group=", group)
    # 四组特征的标签
    labels = ['爱情片', '爱情片', '动作片', '动作片']
    return group, labels


"""
函数说明：KNN算法，分类器-------简单KNN-----------

:parameter:
    inX -用于分类的数据(测试集)
    dataSet -用于训练的数据(训练集)
    labels -分类标签
    k - knn算法参数，选择距离最小的K个点
Returns:
    sortedClassCount[0][0] -分类结果
    
"""


def classify0(inX, dataSet, labels, k):
    # 获取dataSet的行数
    dateSetSize = dataSet.shape[0]
    # 在列方向上重复inX共1次，在行向量方向上重复in重复dataSize次，使之匹配dataSet的大小
    diffMat = np.tile(inX, (dateSetSize, 1)) - dataSet
    """
    意思是把[101,20]变成
    101 20
    101 20
    101 20
    101 20
    这样我们就可以利用这个新的矩阵来与dataSet进行欧氏距离的计算
    """
    # 二维特征相减后平方
    sqDiffMat = diffMat ** 2
    # sum()所有元素相加，sum(0)列相加，sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDisIndices = distances.argsort()
    # 定义一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDisIndices[i]]
        # dict.get(key,default=None)，字典的get()方法，返回指定键值，如果值不存在就返回默认值
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    """
    key=operator.itemgetter(1)根据字典的值进行排序
    key=operator.itemgetter(0)根据字典的键进行排序
    """
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回字典中值最大的值所对应的键
    return sortedClassCount[0][0]


if __name__ == '__main__':
    group, labels = createDataSet()
    newMovieIndex1 = [101, 60]
    newMovieIndex2=[60,20]
    movieClass = classify0(newMovieIndex1, group, labels, 3)
    movieClass2 = classify0(newMovieIndex2, group, labels, 3)
    print(movieClass)
    print(movieClass2)
