"""
这是一个基于RNN的google股价预测项目
数据集来源kaggle
链接：https://www.kaggle.com/datasets/shreenidhihipparagi/google-stock-prediction

"""
import keras
import matplotlib_inline
import numpy as np
import pandas as pd

data=pd.read_csv("Google.csv")
price=data.loc[:,'Adj. Close']
price.head()
#归一化
price_norm=price/max(price)

"""
#可视化
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
fig1=plt.figure(figsize=(8,6))
plt.plot(price)
plt.title('close price')
plt.xlabel('time')
plt.ylabel('price')
plt.show()
"""
#define input X and y
def extract_data(data,time_step):
    X=[]
    y=[]
    #0,1,2,3...,9 10个样本；time_step=8  根据前8个样本预测第9个数据
    #第一个样本0,1,2,3,4,5,6,7   预测8
    #第二个样本1,2,3,4,5,6,7,8   预测9

    for i in range(len(data)-time_step):
        X.append([a for a in data[i:i+time_step]])
        y.append(data[i+time_step])
    X=np.array(X)
    X=X.reshape(X.shape[0],X.shape[1],1)#转换成RNN可用的3个维度  分别是【样本数：time_step:每个样本的维度】
    y = np.array(y)
    return X,y

time_step=8
X,y=extract_data(price_norm,time_step)
print(X)
print(y)

#set up the model
from keras.models import Sequential
from keras.layers import Dense,SimpleRNN
model=Sequential()
#add RNN layer
model.add(SimpleRNN(units=20,input_shape=(time_step,1),activation='relu'))
##add output layer
model.add(Dense(units=1,activation='linear'))
#configure the mode
model.compile(optimizer='adam',loss='mean_squared_error')
model.summary()
#train the model
model.fit(X,y,batch_size=100,epochs=300)


#make prediction base on training data
y_train_predict=model.predict(X)*max(price)
y_train=[i*max(price) for i in y]
print(y_train)

#可视化
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
fig1=plt.figure(figsize=(8,6))
plt.plot(y_train,label='real price')
plt.plot(y_train_predict,label='predict price')
plt.title('close price')
plt.xlabel('time')
plt.ylabel('price')
plt.legend()
plt.show()
