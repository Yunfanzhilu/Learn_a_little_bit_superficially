"""
本文件是基于pytorch的rnn练习，参考视频
B站up：刘二大人《PyTorch深度学习实践》，
链接： https://www.bilibili.com/video/BV1Y7411d7Ys?from=search&seid=1631997590037031874&spm_id_from=333.337.0.0

本文将使用pytorch中的RNNCell模块构建rnn
"""
import torch


batch_size=1
seq_len=3
input_size=4
hidden_size=2
num_layers=1

cell=torch.nn.RNN(input_size=input_size,hidden_size=hidden_size,num_layers=num_layers)

#(seqLen,batchSize,inputSize)
inputs=torch.randn(seq_len,batch_size,input_size)
hidden=torch.ones(num_layers,batch_size,hidden_size)

out,hidden=cell(inputs,hidden)

print('Output_size:',out.shape)
print('Output:',out)

print(f"Hidden_size={hidden.shape},Hidden:{hidden}")






