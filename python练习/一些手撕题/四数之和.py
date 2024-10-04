from typing import List
class Solution():
    def  foursum(self,nums:List[int],target:int)->List[List[int]]:
        length=len(nums)
        if length<4:
            return -1
        nums.sort(reverse=False)
        res=[]
        #双指针法
        for i in range(length):
            for j in range(i+1,length):
                left=j+1
                right=length-1
                while left<right:
                    if (nums[i]+nums[j]+nums[left]+nums[right]==target):
                        if [nums[i], nums[j], nums[left], nums[right]] not in res:
                            res.append([nums[i],nums[j],nums[left],nums[right]])
                        else:
                            left+=1
                            right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        left+=1
                    else:
                        right-=1
        return res
                    
Solution_s1=Solution()
li=[1,1,-1,2,5,-2,2,7]

print(Solution_s1.foursum(li,3))



