"""
实战:决策树实现iris数据分类
1.基于iris.csv数据，建立决策树模型，评估模型表现
2.可视化决策树结构
3.修改min_samples_leaf参数，对比模型结果

"""
#导入库函数
import pandas as pd
import numpy as np

#load the data
data=pd.read_csv('iris.csv')

#define X and y
X=data.drop(['species'],axis=1) #去掉最后一列
y=data.loc[:,'species']
print(f"X的维度：{X.shape},y的维度:{y.shape}")

#establish the decision tree
"""
决策树求解
ID3
利用信息熵（entropy）原理选择信息增益最大的属性作为分类属性，
递归地扩展决策树的分枝，完成决策树的构造
"""
from sklearn import tree
dc_tree=tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=10)
dc_tree.fit(X,y)

#evaluate the model
y_predict=dc_tree.predict(X)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y,y_predict)
print(accuracy)

#visualize the tree
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
fig_dc_tree=plt.plot(figsize=(10,10))
tree.plot_tree(dc_tree,filled='True',feature_names=['sepal_length','sepal_width','petal_length','petal_width'],class_names=['setosa','versicolor','virginica'])
plt.show()

"""
决策树总结
1.通过建立决策树，可实现对标签数据的有效分类
2.尝试修改min_samples_leaf进行决策树的修改
"""



