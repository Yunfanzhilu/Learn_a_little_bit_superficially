
"""
小练习：
训练一个模型seq~seq
hello->ohlol
"""
import torch

batch_size=1
seq_len=5
input_size=5
hidden_size=5
num_layers=1
class Model(torch.nn.Module):
    def __init__(self,input_size,hidden_size,batch_size,num_layers=1):
        super(Model,self).__init__()
        self.num_layers=num_layers
        self.batch_size=batch_size
        self.input_size=input_size
        self.hidden_size=hidden_size
        self.rnn=torch.nn.RNN(input_size=self.input_size,
                              hidden_size=self.hidden_size,
                              num_layers=num_layers)

    def forward(self,input):
        hidden=torch.zeros(self.num_layers,self.batch_size,self.hidden_size)#构造h0 shape[numLayers,batchSize,hiddenSize]
        out,_=self.rnn(input,hidden)#out是 RNN 的输出，它包含了每个时间步的隐藏状态。
                                    #_通常是一个占位符，用于接收一个可能返回但在这里不被使用的值，比如 RNN 的最终隐藏状态（如果 RNN 返回最终隐藏状态和输出的话）。
        return out.view(-1,self.hidden_size) #-1表示自动计算该维度的大小，使得总元素数量不变。这里将输出形状从原始的序列长度、批处理大小和隐藏状态大小调整为(seqLen * batchSize, hiddenSize)，即将序列长度和批处理大小两个维度合并为一个维度，以便后续的处理或作为模型的最终输出。

net=Model(input_size,hidden_size,batch_size,num_layers)

inputData="nihao"
outputData='haoni'
inputData=list(inputData)
x_data=[]
y_data=[]
dict={b:a for a,b in enumerate(inputData)}
for i in range(len(inputData)):
    x_data.append(dict[inputData[i]])
    y_data.append(dict[outputData[i]])

idx2char=['n','i','h','a','o']

one_hot_lookup=[[1,0,0,0,0],
                [0,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,0],
                [0,0,0,0,1]]

x_one_hot=[one_hot_lookup[x] for x in x_data]

inputs=torch.Tensor(x_one_hot).view(seq_len,batch_size,input_size)
labels=torch.LongTensor(y_data)

criterion=torch.nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(net.parameters(),lr=0.06)
for epoch in range(20):
    optimizer.zero_grad()
    outputs=net(inputs)
    loss=criterion(outputs,labels)
    loss.backward()
    optimizer.step()
    #设置输出
    _,idx=outputs.max(dim=1)
    idx=idx.data.numpy()
    print('predicted:',''.join([idx2char[x] for x in idx]),end='')
    print(', Epoch [%d/20]loss=%.3f'%(epoch+1,loss.item()))
