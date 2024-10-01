# -*- coding: UTF-8 -*-

from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import operator
import matplotlib

matplotlib.use('TkAgg')

"""
函数说明:kNN算法,分类器

Parameters:
	inX - 用于分类的数据(测试集)
	dataSet - 用于训练的数据(训练集)
	labes - 分类标签
	k - kNN算法参数,选择距离最小的k个点
Returns:
	sortedClassCount[0][0] - 分类结果

"""


def classify0(inX, dataSet, labels, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    # 在列向量方向上重复inX共1次(横向),行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 二维特征相减后平方
    sqDiffMat = diffMat ** 2
    # sum()所有元素相加,sum(0)列相加,sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方,计算出距离
    distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    # 定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # python3中用items()替换python2中的iteritems()
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]


"""
函数说明:打开并解析文件，对数据进行分类

Parameters:
	filename - 文件名
Returns:
	returnMat - 特征矩阵
	classLabelVector - 分类Label向量

"""


def file2matrix(filename):
    # 打开文件,此次应指定编码，

    fr = open(filename, 'r', encoding='utf-8')
    # 读取文件所有内容
    arrayOLines = fr.readlines()
    # 针对有BOM的UTF-8文本，应该去掉BOM，否则后面会引发错误。
    arrayOLines[0] = arrayOLines[0].lstrip('\ufeff')
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 返回的NumPy矩阵,解析完成的数据:numberOfLines行,3列
    returnMat = np.zeros((numberOfLines, 5))
    # 返回的分类标签向量
    classLabelVector = []
    # 行的索引值
    index = 0

    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        listFromLine = line.split(' ')
        # 将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
        returnMat[index, :] = listFromLine[0:5]
        # 根据文本中标记的等级,1代表垃圾球员,2代表普通球员，3代表全明星球员
        # 最后的标签是已经经过处理的 标签已经改为了1, 2, 3
        if listFromLine[-1] == 'UselessPlayer':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'AveragePlayer':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'All-StarPlayer':
            classLabelVector.append(3)
        index += 1
    # print("returnMat=",returnMat)
    # print("classLabelVector=",classLabelVector)
    return returnMat, classLabelVector


"""
函数说明:可视化数据

Parameters:
	datingDataMat - 特征矩阵
	datingLabels - 分类Label
Returns:
	无

"""


def showdatas(datingDataMat, datingLabels):
    # 设置汉字格式
    font = FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc", size=14)  ##需要查看自己的电脑是否会包含该字体
    # 将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
    # 当nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(8, 8))

    numberOfLabels = len(datingLabels)
    LabelsColors = []
    for i in datingLabels:
        if i == 1:
            LabelsColors.append('black')
        if i == 2:
            LabelsColors.append('green')
        if i == 3:
            LabelsColors.append('blue')
    # 画出散点图,以datingDataMat矩阵的第一(得分)、第二列(篮板)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][0].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 1], color=LabelsColors, s=15, alpha=.5)
    # 设置标题,x轴label,y轴label
    axs0_title_text = axs[0][0].set_title(u'得分与篮板', fontproperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(u'', fontproperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'', fontproperties=font)
    plt.setp(axs0_title_text, size=9, weight='bold', color='red')

    # 设置图例
    UselessPlayer = mlines.Line2D([], [], color='black', marker='.',
                                  markersize=6, label='UselessPlayer')
    AveragePlayer = mlines.Line2D([], [], color='green', marker='.',
                                  markersize=6, label='AveragePlayer')
    All_StarPlayer = mlines.Line2D([], [], color='blue', marker='.',
                                   markersize=6, label='All-StarPlayer')
    # 添加图例
    axs[0][0].legend(handles=[UselessPlayer, AveragePlayer, All_StarPlayer])

    # 显示图片
    plt.show()


"""
函数说明:对数据进行归一化

Parameters:
	dataSet - 特征矩阵
Returns:
	normDataSet - 归一化后的特征矩阵
	ranges - 数据范围
	minVals - 数据最小值

"""


def autoNorm(dataSet):
    # 获得数据的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 最大值和最小值的范围
    ranges = maxVals - minVals
    # shape(dataSet)返回dataSet的矩阵行列数
    normDataSet = np.zeros(np.shape(dataSet))
    # 返回dataSet的行数
    m = dataSet.shape[0]
    # 原始值减去最小值
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # 除以最大和最小值的差,得到归一化数据
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    # 返回归一化数据结果,数据范围,最小值
    return normDataSet, ranges, minVals


"""
函数说明:分类器测试函数
取百分之十的数据作为测试数据，检测分类器的正确性

Parameters:
	无
Returns:
	无

"""


def NBAPlayerClassTest():
    # 打开的文件名
    filename = "NBAPlayers.txt"
    # 将返回的特征矩阵和分类向量分别存储到datingDataMat和datingLabels中
    datingDataMat, datingLabels = file2matrix(filename)
    showdatas(datingDataMat, datingLabels)
    # 取所有数据的百分之十
    hoRatio = 0.10
    # 数据归一化,返回归一化后的矩阵,数据范围,数据最小值
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 获得normMat的行数
    m = normMat.shape[0]
    # 百分之十的测试数据的个数
    numTestVecs = int(m * hoRatio)
    # 分类错误计数
    errorCount = 0.0

    for i in range(numTestVecs):
        # 前numTestVecs个数据作为测试集,后m-numTestVecs个数据作为训练集
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 4)
        print("分类结果:%s\t真实类别:%d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("错误率:%f%%" % (errorCount / float(numTestVecs) * 100))


"""
函数说明:通过输入一个人的三维特征,进行分类输出

Parameters:
	无
Returns:
	无

Modify:
	2017-03-24
"""


def classifyPerson():
    # 输出结果
    resultList = ['垃圾球员', '普通球员', '全明星球员']
    """
    # 五维特征用户输入
    points = float(input("得分"))
    rebounds = float(input("篮板"))
    assists = float(input("助攻"))
    steals = float(input("抢断"))
    blocks = float(input("盖帽"))
    """
    # 打开的文件名
    filename = "NBAPlayers.txt"
    # 打开并处理数据
    playerData, playerLabels = file2matrix(filename)
    # 训练集归一化
    normMat, ranges, minVals = autoNorm(playerData)
    # 生成NumPy数组,测试集
    # inArr = np.array([points, rebounds, assists,steals,blocks])
    inArr_player1 = np.array([20, 10, 10, 2, 2])
    inArr_player2 = np.array([2, 1, 1, 2, 2])
    inArr_player3 = np.array([11, 7, 6, 2, 2])
    # 测试集归一化
    norminArr1 = (inArr_player1 - minVals) / ranges
    norminArr2 = (inArr_player2 - minVals) / ranges
    norminArr3 = (inArr_player3 - minVals) / ranges
    # 返回分类结果
    classifierResult1 = classify0(norminArr1, normMat, playerLabels, 3)
    classifierResult2 = classify0(norminArr2, normMat, playerLabels, 3)
    classifierResult3 = classify0(norminArr3, normMat, playerLabels, 3)

    # 打印结果
    print("球员1可能是%s" % (resultList[classifierResult1 - 1]))
    print("球员2可能是%s" % (resultList[classifierResult2 - 1]))
    print("球员3可能是%s" % (resultList[classifierResult3 - 1]))


"""
函数说明:main函数

Parameters:
	无
Returns:
	无

Modify:
	2017-03-24
"""
if __name__ == '__main__':
    NBAPlayerClassTest()
    classifyPerson()
