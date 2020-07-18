# AUTHOR lijixin
#1
import importlib
#2
import trees
#3
from math import log
#4
import operator
#5
#6
def calcShannonEnt(dataset):
#7
numEntries = len(dataset)
#8
labelCounts = {}
#9
for featVec in dataset:
#10
currentLabel = featVec[-1]
#11
if currentLabel not in labelCounts.keys():
#12
labelCounts[currentLabel] = 0
#13
labelCounts[currentLabel]+=1
#14
shannoEnt = 0.0
#15
for key in labelCounts:
#16
prob = float(labelCounts[key])/numEntries
#17
shannoEnt -=prob*log(prob,2)
#18
return shannoEnt
#19
#20
def splitDataSet(dataSet,axis,value):
#21
retDataSet = []
#22
for featVec in dataSet:
#23
if featVec[axis] == value:
#24
reduceFeatVec = featVec[:axis]
#25
reduceFeatVec.extend(featVec[axis+1:])
#26
retDataSet.append(reduceFeatVec)
#27
return retDataSet
#28
#29
def createDataSet():
#30
dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
#31
lables = ['no surfacing','flippers']
#32
return dataSet,lables
#33
#34
def chooseBestFeatureToSplit(dataSet):
#35
numFeatures = len(dataSet[0])-1
#36
baseEntropy = calcShannonEnt(dataSet)
#37
bestInfoGain = 0.0;bestFeature = -1
#38
for i in range(numFeatures):
#39
featList = [example[i] for example in dataSet]
#40
uniqueVals = set(featList)
#41
newEntropy = 0.0
#42
for value in uniqueVals:
#43
subDataSet = splitDataSet(dataSet,i,value)
#44
prob = len(subDataSet)/ float(len(dataSet))
#45
newEntropy += prob* calcShannonEnt(subDataSet)
#46
infoGain = baseEntropy - newEntropy
#47
if(infoGain > bestInfoGain):
#48
bestInfoGain = infoGain
#49
bestFeature = i
#50
return bestFeature
#51
#52
def majorityCnt(classList):
#53
classCount = {}
#54
for vote in classList:
#55
if vote not in classCount.keys():classCount[vote]= 0
#56
classCount[vote]+=1
#57
sortedClassCount = sorted(classCount.iteritems(),\
#58
key=operator.itemgetter(1),reverse=True)
#59
return sortedClassCount[0][0]
#60
#61
def createTree(dataSet,labels):
#62
classList = [example[-1] for example in dataset]
#63
if classList.count(classList[0]) == len(classList):
#64
return classList[0]
#65
if len(dataSet[0]) == 1:
#66
return majorityCnt(classList)
#67
bestFeatLabel = labels[be]
#68
#69
#70
#71
#72
if __name__=="__main__":
#73
importlib.reload(trees)
#74
myDat, lables = trees.createDataSet()
#75
print(myDat)
#76
print(trees.splitDataSet(myDat,0,1))
#77
# print(trees.splitDataSet(myDat,0,0))
#78
# 得到熵 熵越高则混合的数据越多 可以在数据中添加更多的分类，观察熵是如何变化的
#79
# print(calcShannonEnt(myDat))
#80
