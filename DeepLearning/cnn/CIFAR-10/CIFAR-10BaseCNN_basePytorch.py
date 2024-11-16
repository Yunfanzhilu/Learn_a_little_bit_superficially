import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
import os



class cifar_10_module(nn.Module):
    def __init__(self):
        super(cifar_10_module, self).__init__()
        """
        在Python中，当你定义一个类并继承自另一个类时，你不需要显式地调用父类的构造函数来初始化父类。
        继承会自动完成这一过程。然而，在PyTorch中，由于nn.Module是一个特殊的类，
        它包含了一些重要的初始化代码，比如参数注册等，所以你需要显式地调用super().__init__()来确保这些初始化过程被执行。
        """
        """
        self.conv1 = Conv2d(3, 32, 5, padding=2)
        self.maxpooling1 = MaxPool2d(2)
        self.conv2 = Conv2d(32, 32, 5, padding=2)
        self.maxpooling2 = MaxPool2d(2)
        self.conv3 = Conv2d(32, 64, 5, padding=2)
        self.maxpooling3 = MaxPool2d(2)
        self.flatten = Flatten()
        self.linear1 = Linear(1024, 64)
        self.linear2 = Linear(64, 10)
        """
        self.model1=Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)

        )

    def forward(self, x):
        x=self.model1(x)
        """
        x = self.conv1(x)
        x = self.maxpooling1(x)
        x = self.conv2(x)
        x = self.maxpooling2(x)
        x = self.conv3(x)
        x = self.maxpooling3(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.linear2(x)
        """
        return x

cifar_10_module = cifar_10_module()
print(cifar_10_module)
input= torch.randn((64, 3, 32, 32))
output = cifar_10_module(input)
print(output.shape)
#保存模型参数
torch.save(cifar_10_module.state_dict(),"module1.pth")
#加载模型参数
#加载模型参数
cifar_10_module.load_state_dict("cifar_10_module_epoch1")


