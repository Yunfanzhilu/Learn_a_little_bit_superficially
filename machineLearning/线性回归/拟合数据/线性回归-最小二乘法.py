

"""
基于Sklearn求解线性回归拟合二次多项式,sklearn中使用最小二乘法进行线性回归
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 生成二次多项式形态随机数据集

def data():
    x=np.linspace(0,10,200)
    """
    np.random.normal(loc=0, scale=10, size=None)是函数的调用形式。其中：
    loc=0：表示正态分布的均值为 0。
    scale=10：表示正态分布的标准差为 10。
    size=x.shape：表示生成的随机数组的形状与变量x的形状相同。这里x.shape返回的是一个元组，描述了x的维度信息。
    """
    noise=np.random.normal(loc=0,scale=10,size=x.shape)
    y=x**2+2*x+noise
    return x,y

x,y=data()


#绘制散点图
plt.figure(figsize=(8,8))
plt.scatter(x,y,c='blue',marker='o',label="Data Point")
plt.title("points")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

x6=32+2
#定义要拟合的函数，二次多项式
def func(x,a,b,c):
    return a*x**2+b*x+c

#构建特征矩阵
X = np.column_stack((x**2, x, np.ones_like(x)))

#通过线性回归拟合曲线
model=LinearRegression()
model.fit(X,y)
a=model.coef_[0]
b=model.coef_[1]
c=model.intercept_

# 生成拟合曲线的点
x_fit = np.linspace(0, 10, 200)
y_fit = func(x_fit, a, b, c)

# 绘制拟合曲线
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')
plt.legend()
plt.show()

#对新数据做预测
x_new=[10,20]
new_data = np.array([[i**2, i, 1] for i in x_new])
predictions = model.predict(new_data)
print(new_data)
print(predictions)



