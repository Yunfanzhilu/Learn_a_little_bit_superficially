class Solution:
    def maxProfit(self, prices):
        length=len(prices)
        dp=[[0,0] for _ in range(length)]
        if length<=1:
            return -1
        if length==2 and prices[0]>prices[1]:
            return -1
        for i in range(length):
            if i-1==-1:
                dp[i][0]=0
                dp[i][1]=-prices[i]
            else:
                dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
                dp[i][1]=max(dp[i-1][1],-prices[i])
        return dp[length-1][0]
            
s1=Solution()
li=[7,1,5,3,6,4]
print(s1.maxProfit(li))
