import math
import os

"""
来源于李永乐 B站链接
"""
# 假设贷款12万，年利率6%，月利率0.5%

# 以一年为基准计算
interest01 = 120000 * 0.06
print(f"一年为基准计算:{interest01}")

"""
等额本金，即以相等的本金(12万)来计算利息，每月还款本金1万
1月 120000*0.5%=600
2月 110000*0.5%=
3月 100000*0.5%=
...
12月 10000*0.5%
"""
suminterest02 = 0
for i in range(12):
    interest02 = (120000 - (i * 10000)) * 0.005
    print(f"第{i + 1}个月，你需要还的利息为{interest02}")
    suminterest02 = suminterest02 + interest02

print(f"如果等额本金计算利息为:{suminterest02}")

"""
等额本息，即每个月还的本金和利息是不变的
假设每个月的欠款是a0,a1,a2...a12,其中a12=0
每个月的还款额A(本金+利息)

1月 a0=120000
2月 a1=a0*(1+0.005)-A
3月 a2=a1*(1+0.005)-A
...
12月 a12=a11*(1+0.005)-A=0
"""
suminterest03 = 0
for A in range(120000):
        a0=120000
        a1=a0*(1+0.005)-A
        a2 = a1*(1 + 0.005) - A
        a3 = a2*(1 + 0.005) - A
        a4 = a3*(1 + 0.005) - A
        a5 = a4*(1 + 0.005) - A
        a6 = a5*(1 + 0.005) - A
        a7 = a6*(1 + 0.005) - A
        a8 = a7*(1 + 0.005) - A
        a9 = a8*(1 + 0.005) - A
        a10 = a9 * (1 + 0.005) - A
        a11 = a10 * (1 + 0.005) - A
        a12 = a11 * (1 + 0.005) - A
        if 0.5 > a12 > -0.5:
            suminterest03=A
            break

print(f"如果等额本息计算每个月的利息:{suminterest03-10000}，总共的利息:{(suminterest03-10000)*12}")
