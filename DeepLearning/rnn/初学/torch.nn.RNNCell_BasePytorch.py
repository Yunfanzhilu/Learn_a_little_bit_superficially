
"""
本文件是基于pytorch的rnn练习，参考视频
B站up：刘二大人《PyTorch深度学习实践》，
链接： https://www.bilibili.com/video/BV1Y7411d7Ys?from=search&seid=1631997590037031874&spm_id_from=333.337.0.0

本文将使用pytorch中的RNNCell模块构建rnn
"""
import torch

batch_size=6
seq_len=3 #序列长度3 每个样本里面有x1,x2,x3
input_size=4 #x1,x2,x3长度维度为[*,*,*,*]
hidden_size=2 #hidden层，每个hidden维度2 [*,*]
"""
input.shape=[batchSize,inputSize]
output.shape=[batchSize,hiddenSize]

dataset.shape=[seqLen,batchSize,inputSize]
"""

cell=torch.nn.RNNCell(input_size=input_size,hidden_size=hidden_size)

dataset=torch.randn(seq_len,batch_size,input_size)
hidden=torch.zeros(batch_size,hidden_size)

for idx,input in enumerate(dataset):
    print('='*20,idx,'='*20)
    print('Input size:',input_size)

    hidden=cell(input,hidden)
    print('hidden size(batch_size*hidden_size):',hidden.shape)
    print('hidden=',hidden)