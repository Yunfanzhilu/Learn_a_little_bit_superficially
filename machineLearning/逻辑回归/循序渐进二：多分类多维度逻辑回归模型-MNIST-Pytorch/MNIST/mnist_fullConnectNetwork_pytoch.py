
"""
这是一个10分类的MNIST手写数字集合的练习

步骤：
1.Prepare dataset
2.Design model using Class
3.Construct loss and optimizer
4.Training cycle+Test
"""


import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.optim as optim
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
"""
1.Prepare dataset

"""

batch_size=64
"""
加载数据的过程和2分类唯一的区别就是多了一个transform
transforms.ToTensor()作用是转换the PLT Image to tensor
即PLT Image 28*28 pixel[0...255]->pytorch Tensor 1*28*28 pixel[0...1]

"""
transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307,),(0.3081))])

train_dataset=datasets.MNIST(root='./dataset/',train=True,download=True,transform=transform)
train_loader=DataLoader(train_dataset,shuffle=True,batch_size=batch_size)

test_dataset=datasets.MNIST(root='./dataset/',train=False,download=True,transform=transform)
test_loader=DataLoader(test_dataset,shuffle=True,batch_size=batch_size)


"""
2.Design model using Class
"""
class multiClassificationFullyConnectedNetworkModule(torch.nn.Module):
    def __init__(self):
        super(multiClassificationFullyConnectedNetworkModule, self).__init__()
        self.linear1=torch.nn.Linear(784,512)
        self.linear2 = torch.nn.Linear(512, 256)
        self.linear3 = torch.nn.Linear(256, 128)
        self.linear4 = torch.nn.Linear(128, 10)

    def forward(self,x):
        x=x.view(-1,784)
        x=F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        x_notrelu=self.linear4(x) #注意最后一层不做激活函数处理
        return x_notrelu

model=multiClassificationFullyConnectedNetworkModule()


"""
3.Construct loss and optimizer
"""
criterion=torch.nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.01,momentum=0.5)#momentum 冲量


"""
4.Training cycle+Test
"""
def train(epoch):
    running_loss=0.0
    for batch_idx,data in enumerate(train_loader,0):
        inputs,label=data
        optimizer.zero_grad()

        #forward+backwad+update
        output=model(inputs)
        loss=criterion(output,label)
        loss.backward()
        optimizer.step()

        running_loss+=loss.item()
        if batch_idx %300==299:
            print('[%d,%5d] loss:%.3f'%(epoch+1,batch_idx+1,running_loss//300))
            running_loss=0.0

def test():
    correct=0
    total=0
    with torch.no_grad():
        for data in test_loader:
            images,label=data
            output=model(images)
            _,predicted=torch.max(output.data,dim=1)
            total+=label.size(0)
            correct+=(predicted==label).sum().item()
        print("Accuary on test set:%d %%"%(100*correct/total))


if __name__=='__main__':
    for epoch in range(10):
        train(epoch)
        test()
