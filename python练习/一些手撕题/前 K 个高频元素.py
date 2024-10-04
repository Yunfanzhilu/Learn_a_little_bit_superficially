#! /Annaconda/Install/envs/GPU/python.exe 
# _*_ coding utf-8 _*_
# LeetCode 347
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

import collections
from heapq import *
import heapq


# 解法一：利用哈希表进行计数
# class Solution:
#     def topKFrequent(self, nums, k) :
#         hashmap={}
#         for num in nums:
#             hashmap[num]=hashmap.get(num,0)+1
#         TopKFrequencyNums=sorted(hashmap.items(),key=lambda x: (x[1],x[0]),reverse=True)
#         return [TopKFrequencyNums[j][0] for j in range(k)]

##解法二：使用python自带容器类型模块中的计数器及其函数
# class Solution:
#     def topKFrequent(self,nums,k):
#         res=[e[0] for e in collections.Counter(nums).most_common(3)]
#         return res

##解法三：使用计数器构建最小堆，python默认最小堆
# class Solution:
#     def topKFrequent(self,nums,k):
#         dic=collections.Counter(nums)
#         heap,ans=[],[]
#         for i in dic:
#             heapq.heappush(heap,(dic[i],i))
#         for _ in range(len(dic)):
#             ans.append(heapq.heappop(heap)[1])
#         ans.reverse()
#         res=[]
#         res=ans[0:k]
#         return res


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         def sift_down(arr, root, k):
#             """下沉log(k),如果新的根节点>子节点就一直下沉"""
#             val = arr[root] # 用类似插入排序的赋值交换
#             while root<<1 < k:
#                 child = root << 1
#                 # 选取左右孩子中小的与父节点交换
#                 if child|1 < k and arr[child|1][1] < arr[child][1]:
#                     child |= 1
#                 # 如果子节点<新节点,交换,如果已经有序break
#                 if arr[child][1] < val[1]:
#                     arr[root] = arr[child]
#                     root = child
#                 else:
#                     break
#             arr[root] = val

#         def sift_up(arr, child):
#             """上浮log(k),如果新加入的节点<父节点就一直上浮"""
#             val = arr[child]
#             while child>>1 > 0 and val[1] < arr[child>>1][1]:
#                 arr[child] = arr[child>>1]
#                 child >>= 1
#             arr[child] = val

#         stat = collections.Counter(nums)
#         stat = list(stat.items())
#         heap = [(0,0)]

#         # 构建规模为k+1的堆,新元素加入堆尾,上浮
#         for i in range(k):
#             heap.append(stat[i])
#             sift_up(heap, len(heap)-1) 
#         # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
#         for i in range(k, len(stat)):
#             if stat[i][1] > heap[1][1]:
#                 heap[1] = stat[i]
#                 sift_down(heap, 1, k+1) 
#         return [item[0] for item in heap[1:]]


# 利用堆与优先队列的思想
class Solution:
    def topKFrequent(self, nums, k):
        dictnum = {}
        for num in nums:
            dictnum[num] = dictnum.get(num, 0) + 1
        stat = collections.Counter(nums)
        stat2 = list(stat.items())
        heap = [(0, 0)]
        print(stat)
        print(stat2)
        print(stat2[1])
        print(stat2[1][0])
        print(dictnum)
        ##构建规模为k+1的堆，新元素加入堆尾，上浮


S1 = Solution()
li = [6, 6, 1, 1, 1, 7, 7, 7, 7, 7]
print(S1.topKFrequent(li, 2))
