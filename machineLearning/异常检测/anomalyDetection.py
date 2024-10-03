
"""
2d_apple_anomaly_detection_data.csv中有100个正常苹果的横径和纵径数据，以及10个异常数据

实战：
1.基于2d_apple_anomaly_detection_data.csv可视化数据分布情况以及对应的高斯分布的概率密度函数
2.建立模型，实现异常数据点检测
3.可视化异常检测处理结果
4.修改概率密度分布阈值EllipticEnvelope(contamination=0.1)中的contamination，查看阈值改变对结果的影响

"""
#load the data
import pandas as pd
import numpy as np
data=pd.read_csv('2d_apple_anomaly_detection_data.csv')
data.head()


#visualize the tree
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

fig_anomalyDetection=plt.plot(figsize=(10,10))
plt.scatter(data.loc[:,'Diameter_X'],data.loc[:,'Diameter_Y'])
plt.xlabel('Diameter_X')
plt.ylabel('Diameter_Y')
plt.title('appleData')
plt.show()

#define x1 and x2
x1=data.loc[:,'Diameter_X']
x2=data.loc[:,'Diameter_Y']
fig2=plt.figure(figsize=(10,5))
plt.hist(x1,bins=100)
plt.title('Diameter_X distribution')
plt.xlabel('Diameter_X')
plt.ylabel('counts')
plt.show()

fig3=plt.figure(figsize=(10,5))
plt.hist(x2,bins=100)
plt.title('Diameter_Y distribution')
plt.xlabel('Diameter_Y')
plt.ylabel('counts')
plt.show()

#calculate the mean and sigma of x1 and x2  即均值和标准差
x1_mean=x1.mean()
x1_sigma=x1.std()
x2_mean=x2.mean()
x2_sigma=x2.std()
print(f"x1_mean:{x1_mean},x1_sigma:{x1_sigma}")
print(f"x2_mean:{x2_mean},x2_sigma:{x2_sigma}")

#calculate the gaussian distribution px
from scipy.stats import norm
x1_range=np.linspace(0,15,300)
x1_normal=norm.pdf(x1_range,x1_mean,x1_sigma)
print(x1_normal)
fig_px1=plt.figure(figsize=(10,5))
plt.plot(x1_range,x1_normal)
plt.show()

x2_range=np.linspace(0,15,300)
x2_normal=norm.pdf(x2_range,x2_mean,x2_sigma)
print(x1_normal)
fig_px2=plt.figure(figsize=(10,5))
plt.plot(x2_range,x2_normal)
plt.show()

#establish the model and predict
from sklearn.covariance import EllipticEnvelope
ad_model=EllipticEnvelope()#默认阈值10%
ad_model.fit(data)
#make prediction
y_predict=ad_model.predict(data)
print(y_predict)
print(pd.value_counts(y_predict))

#visualize the result
fig_data=plt.figure(figsize=(10,5))
origin_data=plt.scatter(x1,x2,marker='x')
anomaly_data=plt.scatter(x1[y_predict==-1],x2[y_predict==-1],marker='o')

plt.title('anomaly detection result')
plt.xlabel(x1)
plt.ylabel(x2)
plt.legend((origin_data,anomaly_data),('origin_data','anomaly_data'))
plt.show()

#修改高斯概率密度函数阈值
ad_model=EllipticEnvelope(contamination=0.02)
ad_model.fit(data)
#make prediction
y_predict=ad_model.predict(data)
print(y_predict)
print(pd.value_counts(y_predict))

#visualize the result
fig_data_2=plt.figure(figsize=(10,5))
origin_data=plt.scatter(x1,x2,marker='x')
anomaly_data=plt.scatter(x1[y_predict==-1],x2[y_predict==-1],marker='o')

plt.title('anomaly detection result')
plt.xlabel(x1)
plt.ylabel(x2)
plt.legend((origin_data,anomaly_data),('origin_data','anomaly_data'))
plt.show()