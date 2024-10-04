
# print("转换为二进制为：", bin(num))

print("123")
def fun(num):
    res = []
    str1 = ""
    while(num != 0):
        yushu = num % 2
        num = num//2
        res.append(yushu)
    res.reverse()
    return res


ID = 87661
res = []
res = fun(ID)
for i in res:
    print(i)

print("转换为二进制为：", bin(ID))


# 输入一个二进制字符串
binary = input("请输入一个二进制：")
# 使用int()函数将二进制字符串转化为十进制整数
decimal = int(binary, 2)
# 输出转化后的十进制整数
print(decimal)
