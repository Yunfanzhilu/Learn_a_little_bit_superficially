
# _*_ coding utf-8 _*_
# 赵天宇 python算法 归并排序
#时间复杂度O(nlogn)，空间复杂度O(n)

# def merge(li,low,high):
#     low=0
#     lowtemp=0
#     high=len(li)-1
#     templi=[]
#     while lowtemp<=high:
#         if li[lowtemp]<=li[lowtemp+1]:
#             lowtemp+=1
#         else:
#             break
#     mid=lowtemp
#     while low<=mid:
#         if  mid+1<=high and li[low]<li[mid+1] :
#             templi.append(li[low])
#             low+=1
#         elif mid+1>high:
#             for i in range(lowtemp-low+1):
#                 templi.append(li[low])
#                 low+=1
#             break
#         else:
#             templi.append(li[mid+1])
#             mid+=1
#     return templi
        
    
def merge(li,low,mid,high):
    i=low
    j=mid+1
    litemp=[]
    while i<=mid and j<=high:
        if li[i]<li[j]:
            litemp.append(li[i])
            i+=1
        else:
            litemp.append(li[j])
            j+=1
    while i<=mid:
        litemp.append(li[i])
        i+=1
    while j<=high:
        litemp.append(li[j])
        j+=1
    li[low:high+1]=litemp

def merge_sort(li,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)
    



# li=[1,3,5,7,9,11,13,15,2,4,6,8]
# res=merge(li,0,7)
# print(res)

li=[3,1,5,6,2,6,7,12,17]
merge_sort(li,0,len(li)-1)
print(li)




