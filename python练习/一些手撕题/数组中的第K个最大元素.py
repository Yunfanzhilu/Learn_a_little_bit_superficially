class Solution:
    def findKthLargest(self,nums,k):
        nums.sort(reverse=True)
        for i in range(1,k):
            res=nums[i]
        return res

nums=[3,2,1,5,6,4]
S1=Solution()
res=S1.findKthLargest(nums,2)
print(res)


