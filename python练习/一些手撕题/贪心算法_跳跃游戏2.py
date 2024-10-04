def jump(nums):
    max_jump=nums[0]
    i=1
    length=len(nums)
    step=1
    while(i<length):
        if max_jump+nums[max_jump]<i+nums[i]:
            max_jump=i+nums[i]
            step+=1
        if(max_jump+nums[max_jump]>length):
            return step
        i=i+1
    return step

nums=[2,3,1,2,4,2,3]
res=jump(nums)
print(res)       

        

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxPos, end, step = 0, 0, 0
#         for i in range(n - 1):
#             if maxPos >= i:
#                 maxPos = max(maxPos, i + nums[i])
#                 if i == end:
#                     end = maxPos
#                     step += 1
#         return step


        

