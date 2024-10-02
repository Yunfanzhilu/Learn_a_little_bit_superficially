"""
实战1:决策树实现iris数据分类
1.基于iris.csv数据，建立决策树模型，评估模型表现
2.可视化决策树结构
3.修改min_samples_leaf参数，对比模型结果

实战2：

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
from sklearn import tree
dc_tree=tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=3)
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





