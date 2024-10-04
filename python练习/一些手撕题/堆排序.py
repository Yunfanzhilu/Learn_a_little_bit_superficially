#! /usr/bin/env python
# _*_ coding utf-8 _*_
#created by Tony
# Date 2020/10/03


# #堆排序过程
# 1、建立堆
# 2、得到堆顶元素，为最大值
# 3、去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整冲重新使堆有序
# 4、堆顶元素为第二大元素
# 5、重复步骤3，直到堆变空
#


# def sift(li,low,high):
#     """
#     :param li：列表
#     :param low:堆的根节点位置
#     :param high:堆的最后一个元素的位置
#     ：return:
#     """

#     i=low #i最开始指向根节点
#     j=2*i+1#j开始时左孩子
#     tmp=li[low]#把堆顶存起来
#     while j<=high:#只要j位置有数
#         if j+1<=high and li[j+1]>li[j]:
#             j=j+1 #j指向右孩子
#         if li[j]>tmp:
#             li[i]=li[j]
#             i=j
#             j=2*i+1
#         else:
#             break
#     li[i]=tmp#把tmp放到叶子结点上

# def heap_sort(li):
#     n=len(li)
#     ##第一步：建立堆，农村包围城市，从尾部小堆开始建立
#     for i in range((n-2)//2,-1,-1):
#     #i表示建堆的时候调整的部分的根的下标
#         sift(li,i,n-1)
#     #建堆完成
#     for i in range(n-1,-1,-1):
#         #i指向当前堆的最后一个元素
#         li[0],li[i]=li[i],li[0]
#         sift(li,0,i-1)#i-1是新的high


# li=[i for i in range(10)]
# import random
# random.shuffle(li)
# print("原始乱序列表：",li)

# heap_sort(li)
# print("排好序之后的列表：",li)


def sift(li,low,high):
    i=low
    j=2*i+1
    temp=li[low]
    while j<=high:
        if j+1<=high and li[j+1]>li[j]:
            j=j+1
        if temp<li[j]:
            li[i]=li[j]
            i=j
            j=2*i+1
        else:
            break
    li[i]=temp


def heap_sort(li):
    n=len(li)
    ##建立堆
    for i in range((n-2)//2,-1,-1):
        sift(li,i,n-1)
    ##堆排序
    res=[]
    for j in range(n-1,-1,-1):
        li[0],li[j]=li[j],li[0]
        res.append(li[j])
        sift(li,0,j-1)
    return res

l1=[12,6,1,2,8,11,19,29]
print("原始序列：",l1)
res=heap_sort(l1)
print("堆排序之后的序列：",res)





