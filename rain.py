# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 20:36:31 2017

@author: ZYH
"""
#from pylab import *  
#matplotlib and numpy 就不用加加载了 那些函数就直接可以使用 初学不建议使用
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath=("rain.csv")
dataFile=pd.read_csv(filePath)

summary=dataFile.describe()
print(summary)

array=dataFile.iloc[:,1:13].values
#boxplot and show 不用加plt 如果from pylab import *
plt.boxplot(array)
plt.xlabel("month")
plt.ylabel("rain")
plt.show()

#降水趋势
minRings=-1
maxRings=99
nrows=11
#如果加载了pylab 直接plot就可以
for i in range(nrows):
    #dataRow=dataFile.iloc[i,1:13]
    dataRow=array[i,:] #都可以,这里跟matlab一样，需要：代表所有
    labelColor = (dataFile.iloc[i,12] - minRings) / (maxRings - minRings)	
    plt.plot(dataRow,color=plt.cm.RdYlBu(labelColor), alpha=0.5)		
plt.xlabel("Attribute")										
plt.ylabel(("Score"))											
plt.show()	
#相关性
#超出范围自动取所有 corr()计算列的相关系数 不能使用array类型 
#如果加载pylab pd.DataFrame直接写DataFrame
corMat=pd.DataFrame(dataFile.iloc[1:,1:].corr())
plt.pcolor(corMat)
plt.show()
