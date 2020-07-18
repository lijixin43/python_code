# AUTHOR lijixin

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    # 距离计算
    dataSetSize = dataSet.shape[0] #dataSet.shape 行数和列数 shape[0] 输出行数
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) +1
    # 排序
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# 从文本文件取出数据
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    # 读取文件行数
    numberOfLines = len(arrayOLines)
    # 创建返回的Numpy矩阵 三列数据填充为0
    returnMat = zeros((numberOfLines,3))
    # 创建一个新的数组
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
# 归一化数值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape(0)
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

# def datingClassTest():
#     hoRatio = 0.10
#     datingDatMat,datingLabels = file2matrix('datingTestSet.txt')
#     normMat,range,minVals = autoNorm(datingDatMat)
#     m = normMat.shape(0)
#     numTestVecs = int(m* hoRatio)
#     errorCount = 0.0
#     for i in range(numTestVecs):
#         classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],
#                                      datingLabels[numTestVecs:m],3)
#         # print
#





