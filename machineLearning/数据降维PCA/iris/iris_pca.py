"""
PCA实战
1.基于iris,csv 数据，建立knn模型实现数据分类(n_neighbors=3)
2.对数据进行标准化处理，选取一个维度可视化处理后的效果
3.进行与元数据等维度PCA，查看各主成分的方差比例
4.保留合适的主成分，可视化降维后的数据
5.基于降维后的数据建立knn模型，与元数据表现进行对比

PCA如何保留主要信息:偷听后的不同特征数据尽可能分得开(即不相关)
实现原则：使投影后的数据方差最大，因为方差越大数据越分散

计算过程：
1.原始数据预处理(标准化)
2.计算协方差矩阵特征向量及数据在各个特征向量投影后的方差
3.根据需求(任务指定或方差比例)确定降维维度
4.选择k维特征向量，计算数据在其形成空间的投影
"""
import pandas as pd
import numpy as np
data=pd.read_csv('iris.csv')

#define X and y
X=data.drop('species',axis=1)
y=data.loc[:,'species']

#降维前建立knn
from sklearn.neighbors import KNeighborsClassifier
KNN=KNeighborsClassifier(n_neighbors=3)
KNN.fit(X,y)
y_predict=KNN.predict(X)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y,y_predict)
print(accuracy)#0.96

from sklearn.preprocessing import StandardScaler
X_norm=StandardScaler().fit_transform(X)
print(X_norm)

#calcuate the mean the sigma
x1_mean=X.loc[:,'sepal_length'].mean()
x1_norm_mean=X_norm[:,0].mean()
x1_sigma=X.loc[:,'sepal_length'].std()
x1_norm_sigma=X_norm[:,0].std()
print(f"x1_mean:{x1_mean},x1_sigma:{x1_sigma}")
print(f"x1_norm_mean:{x1_norm_mean},x1_norm_sigma:{x1_norm_sigma}")

#visualize the data
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
fig1=plt.figure(figsize=(20,5))
plt.hist(X.loc[:,'sepal_length'],bins=100)
plt.show()

fig2=plt.figure(figsize=(20,5))
plt.hist(X_norm[:,0],bins=100)
plt.show()

#pca analysis
from sklearn.decomposition import PCA
pca=PCA(n_components=X.shape[1])
X_pca=pca.fit_transform(X_norm)
#calculate the variance ratio of each principle components
var_ratio=pca.explained_variance_ratio_
print(var_ratio)
fig3=plt.figure(figsize=(10,5))
plt.bar([1,2,3,4],var_ratio)
plt.xticks([1,2,3,4],['PC1','PC2','PC3','PC4'])
plt.show()

#从"4维数据的方差.png上看到后2维的数据方差小，进行降维处理，保留前2维"
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X_norm)
X_pca.shape

#visualize the pca reslut
fig4=plt.figure(figsize=(10,10))
setosa=plt.scatter(X_pca[:,0][y=='setosa'],X_pca[:,1][y=='setosa'])
versicolor=plt.scatter(X_pca[:,0][y=='versicolor'],X_pca[:,1][y=='versicolor'])
virginica=plt.scatter(X_pca[:,0][y=='virginica'],X_pca[:,1][y=='virginica'])
plt.legend((setosa,versicolor,virginica),('setosa','versicolor','virginica'))
plt.show()

#降维之后再使用knn
#establish knn model and calculation the accuracy

KNN_pca=KNeighborsClassifier(n_neighbors=3)
KNN_pca.fit(X_pca,y)
y_predict=KNN_pca.predict(X_pca)
accuracy=accuracy_score(y,y_predict)
print(accuracy)#0.9466666666666667

