# AUTHOR lijixin

import kNN

# group,labels = kNN.createDataSet()
#
# dic = kNN.classify0([0,0],group,labels,3)
#
# print(dic)
from numpy import array
import matplotlib
import matplotlib.pyplot as plt

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
print(datingDataMat)
fig = plt.figure()
ax = fig.add_subplot(111)
# 取第二列为x轴，第三列为y轴
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()