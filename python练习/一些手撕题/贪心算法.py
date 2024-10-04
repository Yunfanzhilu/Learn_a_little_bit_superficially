#/urs/bin
#_*_coding uft-8_*_
#Date
#贪心算法


#change_money_找零问题
# t=[100,50,20,1,5]

# def change(t,n):
#     m=[0 for _ in range(len(t))]
#     print(m)
#     for i,money in enumerate(t):
#         m[i]=n
#         n=n%money
#     return m,n

# print(change(t,376))

# def change(t,n):
#     t.sort(reverse=True)
#     print(t)
#     m=[0 for _ in range(len(t))]
#     for i,money in enumerate(t):
#         m[i]=n
#         n=n%money
#     return n,m

# print(change(t,381))    


#分数背包
goods=[(60,10),(100,20),(120,30)]#商品元组（价格，重量）
# goods.sort(key=lambda x:x[0]/x[1],reverse=True)
# def fractional_backpack(goods,w):
#     m=[0 for _ in range(len(goods))]
#     total_v=0
#     for i ,(price,weight) in enumerate(goods):
#         if w>=weight:
#             m[i]=1
#             total_v+=price
#             w-=weight
#         else:
#             m[i]=w/weight
#             total_v+=m[i]*price
#             w=0
#             break
#     return m,total_v

goods.sort(key=lambda x:x[0]/x[1],reverse=True)
def fractional_backpack(goods,w):
    m=[0 for _ in range(len(goods))]
    total_sum=0
    for i,(money,weight) in enumerate(goods):
        if w>weight:
            m[i]=1
            total_sum+=money
            w-=weight
        else:
            m[i]=w/weight
            total_sum+=money*m[i]
            w-=weight
            break
    return m,total_sum


print(fractional_backpack(goods,50))
    
    






