

"""
多维度2分类全连接网络逻辑回归模型
Mutiple Dimension Logistic Regression Model
数据集 iris.csv(修改一下，只保留2种类别)   输入4维，输出1维

步骤：
1.Prepare dataset
2.Design model using Class
3.Construct loss and optimizer
4.Training cycle

"""
from sklearn import linear_model
import torch
from torch.utils.data import Dataset  #Dataset是抽象类，不能实例化，只能被子类继承
from torch.utils.data import DataLoader
import os
import numpy as np


"""
1.Prepare dataset
"""

"""
Xy=np.loadtxt("iris.csv",delimiter=',',dtype=np.float32)
X=torch.from_numpy(Xy[:,:-1])#所有行，第一列开始，最后一列不要
y=torch.from_numpy(Xy[:,[-1]])#左右行，最后一列，[]表示需要矩阵，不写的话就是向量

"""
class irisDataset(Dataset):
    def __init__(self,filepath):
        self.Xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.X = torch.from_numpy(self.Xy[:, :-1])  # 所有行，第一列开始，最后一列不要
        self.y = torch.from_numpy(self.Xy[:, [-1]])  # 左右行，最后一列，[]表示需要矩阵，不写的话就是向量


    def __getitem__(self, index):
        return self.X[index],self.y[index]

    def __len__(self):
        self.len = self.Xy.shape[0]
        return self.len

dataset=irisDataset('iris.csv')
train_loader=DataLoader(dataset=dataset,batch_size=32,shuffle=True)


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

含义
epoch:
One forward pass and one backward pass of all the training exanples

Batch_size:
The number of training examples in one forward backward pass

Iteration
Number of passed,each pass using[batch size]numbelr of examples

epoch是把所有样本都做一次前馈反馈，是一个训练周期

batch是对原样本进行打包

batch_size是每一个包的大小

iteration是在这一个训练周期内，训练完所有包需要的迭代次数

"""

for epoch in range(1000):
    for i,data in enumerate(train_loader,0): #loader中data会自动变成Tensor
        #1.prepare data
        inputs,labels=data

        #2.forward
        y_pred=model(inputs)
        loss=criterion(y_pred,labels)
        print(epoch,i,loss.item())

        #3.backward
        optimizer.zero_grad()
        loss.backward()

        #4.update
        optimizer.step()





