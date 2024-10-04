class Solution(object):
    def TopKFrequency(self,nums,k):
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        TopKFrequencyNums=sorted(hashmap.items(),key=lambda x: (x[1],x[0]),reverse=True)
        return [TopKFrequencyNums[j][0] for j in range(k)]




li=[71,71,71,71,71,71,88,88,88,91,91,106,106]
Solution1=Solution()
res=Solution1.TopKFrequency(li,2)
print(res)
