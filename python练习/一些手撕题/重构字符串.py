#! /Annaconda/Install/envs/GPU/python.exe 
# _*_ coding utf-8 _*_
# LeetCode 767
import heapq

class Solution(object):
    def reorganizeString(self, S):
        pq= [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        # pq=[]
        # heapq.heappush(pq,pq1)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        res="".join(ans) + (pq[0][1] if pq else '')
        return res

S1=Solution()
str1="aab"
res=S1.reorganizeString(str1)
print(res)