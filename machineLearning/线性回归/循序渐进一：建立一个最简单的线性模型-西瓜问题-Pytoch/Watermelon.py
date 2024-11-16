"""
任务名称：西瓜价格预测
数据集："Watermelon.csv"
描述：基于pytorch建立线性回归模型，预测10kg西瓜的价格
"""



import torch

#WatermelonData=pd.read_csv("Watermelon.csv")
#WatermelonData.head()
#x = list(WatermelonData.loc[:, 'Watermeon size/kg'])
#y = list(WatermelonData.loc[:, 'Watermeon prices/RMB'])

"""
Step1:
Prepare dataset
"""
x=[1,2,3]
y=[6,9,12]
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

    def forward(self,x):
        y_pred=self.linear(x)
        return y_pred

watermelonModule=watermelonModule()

"""
step3:
Construct loss and optimizer
"""
criterion=torch.nn.MSELoss(size_average=False)
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

x_test=torch.Tensor([98])
y_test=watermelonModule(x_test)
print("y_pred=",y_test)


