from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

housing_data = pd.read_csv('boston_house_price_english.csv')
housing_data.head()
X = housing_data.drop(['medv'],axis = 1)
y = housing_data['medv']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=888) # 随机数种子：random_state
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train) # 用此线性回归模块在训练集上进行拟合

lin_reg.score(X_test, y_test) # 在用这个模块对测试集进行评估
lin_reg.coef_  # 用这个属性可以输出13个列数据的斜率

ans=lin_reg.predict(X_test) # 用此线性回归模型对测试集上的特征进行预测  # 这是预测的房价
deviation = ans- y_test  # 预测值与实际值的偏差