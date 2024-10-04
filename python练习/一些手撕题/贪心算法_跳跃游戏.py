

#如果从该位置到达的最远位置越过了数组中的0，这个0就不影响最终的结果了，而如果发现从某位置可以到达数组的最后一个位置，说明该问题有解
#位置i能够到达的最远位置
def canJump(nums):
    if(len(nums)==0 or nums[0]==0):
        return False
    index=0
    jump=[0 for x in range(0,len(nums))]
    jump[0]=0+nums[0]
    for index in range(len(nums)):
        jump[index]=index+nums[index]
    max_jump=jump[0]
    index=0
    while(index<len(jump)-1 and index<=max_jump):
        if(jump[index]>max_jump):
            max_jump=jump[index]
        index=index+1
    if(index==len(jump)-1):
        return True
    else:
        return False


def canJump2(nums):
    i=0
    max_jump=0
    res=0
    for index,value in enumerate(nums):
        if(index<len(nums) and index+value>max_jump):
            max_jump=index+value
            res+=1
    return res


nums=[2,4,2,3,1,0,0]
res=canJump2(nums)
print(res)






