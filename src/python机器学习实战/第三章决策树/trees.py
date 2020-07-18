# AUTHOR lijixin
import importlib
import trees
from math import log
import operator

def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    shannoEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannoEnt -=prob*log(prob,2)
    return shannoEnt

def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    lables = ['no surfacing','flippers']
    return dataSet,lables

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/ float(len(dataSet))
            newEntropy += prob* calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]= 0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.iteritems(),\
                              key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeatLabel = labels[be]




if __name__=="__main__":
    importlib.reload(trees)
    myDat, lables = trees.createDataSet()
    print(myDat)
    print(trees.splitDataSet(myDat,0,1))
    # print(trees.splitDataSet(myDat,0,0))
    # 得到熵 熵越高则混合的数据越多 可以在数据中添加更多的分类，观察熵是如何变化的
    # print(calcShannonEnt(myDat))
