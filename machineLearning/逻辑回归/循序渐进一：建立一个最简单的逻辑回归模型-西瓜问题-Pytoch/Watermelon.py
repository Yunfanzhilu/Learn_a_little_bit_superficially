"""
任务名称：西瓜价格预测
数据集："Watermelon.csv"
描述：基于pytorch建立逻辑回归模型，预测10kg西瓜是个大西瓜还是小西瓜
"""
import numpy as np
import torch

#WatermelonData=pd.read_csv("Watermelon.csv")
#WatermelonData.head()
#x = list(WatermelonData.loc[:, 'Watermeon size/kg'])
#y = list(WatermelonData.loc[:, 'Watermeon prices/RMB'])

"""
Step1:
Prepare dataset
"""
x=[1,2,3,4,5]
y=[0,0,0,1,1] #标签0代表小西瓜，1代表大西瓜
x_data = torch.Tensor([[float(i)] for i in x])
y_data = torch.Tensor([[float(i)] for i in y])
print(f"x={x_data}\ny={y_data}")


"""
Step2:
Design model using Class
"""
class watermelonModule(torch.nn.Module):
    def __init__(self):
        super(watermelonModule, self).__init__()
        self.linear=torch.nn.Linear(1,1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self,x):
        y_pred=self.sigmoid(self.linear(x))
        return y_pred

watermelonModule=watermelonModule()

"""
step3:
Construct loss and optimizer
"""
criterion=torch.nn.BCELoss(size_average=False)
optimizer=torch.optim.SGD(watermelonModule.parameters(),lr=0.01)

"""
step4:
Training cycle
"""

for epoch in range(10000):
    y_pred=watermelonModule(x_data)
    loss=criterion(y_pred,y_data)
    print(epoch,loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("w=",watermelonModule.linear.weight.item())
print("b=",watermelonModule.linear.bias.item())


"""
step5:
predict new data
"""
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
x=np.linspace(0,10,200)
x_t=torch.Tensor(x).view((200,1))
y_t=watermelonModule(x_t)
y=y_t.data.numpy()
plt.plot(x,y)
plt.plot([0,10],[0.5,0.5],c='r')
plt.xlabel("size")
plt.ylabel("Big or Small")
plt.grid()
plt.show()


