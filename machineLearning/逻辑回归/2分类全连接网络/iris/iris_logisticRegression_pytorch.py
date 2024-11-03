

"""
多维度逻辑回归模型(加入batch)
Mutiple Dimension Logistic Regression Model
数据集 2分类全连接网络.csv   输入4维，输出1维

步骤：
1.Prepare dataset
2.Design model using Class
3.Construct loss and optimizer
4.Training cycle

"""
from sklearn import linear_model
import torch
import numpy as np


"""
1.Prepare dataset
"""

Xy=np.loadtxt("2分类全连接网络.csv",delimiter=',',dtype=np.float32)
X=torch.from_numpy(Xy[:,:-1])#所有行，第一列开始，最后一列不要
y=torch.from_numpy(Xy[:,[-1]])#左右行，最后一列，[]表示需要矩阵，不写的话就是向量

"""
2.Design model using Class
"""
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1=torch.nn.Linear(4,2) #矩阵是空间变换的函数，这里任意4维空间的向量线性映射到2维空间
        self.linear2 = torch.nn.Linear(2, 1)
        self.sigmoid=torch.nn.Sigmoid()#神经网络本质就是找非线性的空间变换的函数，所以这里加入非线性的激活函数

    def forward(self,x):
        x=self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        return x

model=Model()

"""
3.Construct loss and optimizer
"""

criterion=torch.nn.BCELoss(size_average=True)
optimizer=torch.optim.SGD(model.parameters(),lr=0.1)

"""
4.Training cycle



"""
for epoch in range(1000):
    #forward
    y_pred=model(X)
    loss=criterion(y_pred,y)
    print(epoch,loss.item())

    #backward
    optimizer.zero_grad()
    loss.backward()

    #update
    optimizer.step()





