"""
该项目是芯片检测的模型
使用逻辑回归的思想进行检测分类
本练习数据集chip_test.csv
"""
# load the data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
data = pd.read_csv('chip_test.csv')


#add label mask
mask=data.loc[:,'pass']==1



#define X,y
X=data.drop('pass',axis=1)#把pass列去掉
y=data.loc[:,'pass']
X1 = data.loc[:, 'test1']
X2 = data.loc[:, 'test2']


#establish the model and train it
from sklearn.linear_model import  LogisticRegression
chipLR=LogisticRegression()
chipLR.fit(X,y)

#show the predicted result and its accuracy
y_predict=chipLR.predict(X)
print(y_predict)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y,y_predict)
print(accuracy)

"""
# visualize the data
theta0=chipLR.intercept_
theta1,theta2=chipLR.coef_[0][0],chipLR.coef_[0][1]
X2_new=(theta0+theta1*X1)/theta2
fig1 = plt.figure()
test01 = data.loc[:, 'test1']
test02 = data.loc[:, 'test2']
passed=plt.scatter(test01[mask],test02[mask])
failed=plt.scatter(test01[~mask],test02[~mask])
plt.plot(X1,X2_new)
plt.title('test1-test2')
plt.xlabel('test1')
plt.ylabel('test2')
plt.legend((passed,failed),('passed','failed'))
plt.show()
"""
"""
一阶的决策函数 theta0+theta1*x+theta2*x2=0的表现并不好，以下采用二阶函数进行决策
"""

#create new data
X1_2=X1*X1
X2_2=X2*X2
X1_X2=X1*X2
X_new={'X1':X1,'X2':X2,'X1_2':X1_2,'X2_2':X2_2,'X1_X2':X1_X2}
X_new=pd.DataFrame(X_new)
print(X_new)

LR2=LogisticRegression()
LR2.fit(X_new,y)
y2_predict=LR2.predict(X_new)
accuracy2=accuracy_score(y,y2_predict)
print(accuracy2)

X1_new=X1.sort_values()
theta0=LR2.intercept_
theta1,theta2,theta3,theta4,theta5=LR2.coef_[0][0],LR2.coef_[0][1],LR2.coef_[0][2],LR2.coef_[0][3],LR2.coef_[0][4]
a=theta4
b=theta5*X1_new+theta2
c=theta0+theta1*X1_new+theta3*X1_new*X1_new
X2_new_boundary_1=(-b+np.sqrt(b*b-4*a*c))/(2*a)

X2_new_boundary_2=(-b-np.sqrt(b*b-4*a*c))/(2*a)



fig1 = plt.figure()
test01 = data.loc[:, 'test1']
test02 = data.loc[:, 'test2']
passed=plt.scatter(test01[mask],test02[mask])
failed=plt.scatter(test01[~mask],test02[~mask])
plt.plot(X1_new,X2_new_boundary_1)
plt.plot(X1_new,X2_new_boundary_2)
plt.title('test1-test2')
plt.xlabel('test1')
plt.ylabel('test2')
plt.legend((passed,failed),('passed','failed'))
plt.show()
