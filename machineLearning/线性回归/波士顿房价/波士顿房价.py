
"""
波士顿房价数据集简介

CRIM--城镇人均犯罪率                                                              ------【城镇人均犯罪率】
ZN - 占地面积超过25,000平方英尺的住宅用地比例。               ------【住宅用地所占比例】
INDUS - 每个城镇非零售业务的比例。                                      ------【城镇中非商业用地占比例】
CHAS - Charles River虚拟变量（如果是河道，则为1;否则为0  ------【查尔斯河虚拟变量，用于回归分析】
NOX - 一氧化氮浓度（每千万份）                                             ------【环保指标】
RM - 每间住宅的平均房间数                                                      ------【每栋住宅房间数】
AGE - 1940年以前建造的自住单位比例                                     ------【1940年以前建造的自住单位比例 】
DIS -波士顿的五个就业中心加权距离                                        ------【与波士顿的五个就业中心加权距离】
RAD - 径向高速公路的可达性指数                                             ------【距离高速公路的便利指数】
TAX - 每10,000美元的全额物业税率                                          ------【每一万美元的不动产税率】
PTRATIO - 城镇的学生与教师比例                                             ------【城镇中教师学生比例】
B - 1000（Bk - 0.63）^ 2其中Bk是城镇黑人的比例                   ------【城镇中黑人比例】
LSTAT - 人口状况下降％                                                            ------【房东属于低等收入阶层比例】
MEDV - 自有住房的中位数报价, 单位1000美元                         ------【自住房屋房价中位数】


"""

from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

housing_data = pd.read_csv('BostonHousing.csv')
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