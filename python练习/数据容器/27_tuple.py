
"""
1.元组(tuple)可以存放多个不同类型数据，元组是「不可变序列」
即创建之后就不能改变，不能增删改没有append(),insert()这样的方法
「但又获取某个索引值的方法，但不能重新赋值」
"""
tuple_a=(100,200,300)
print(f"tuple_a元组的内容：{tuple_a},tuple_a的类型：{type(tuple_a)}")


"""元组循环输出"""
index=0
while index<len(tuple_a):
    print(f"while循环遍历元素：{tuple_a[index]}")
    index+=1
for ele in tuple_a:
    print(f"for循环遍历元素是:{ele}")

print("="*30)

"""
元组的元素可以有多个，数据类型有没有限制？允不允许重复元素，是不是有序的？
元组可以嵌套元组
"""
tuple_c=(100,"blue",7.3,True,'a',100,'blue',tuple_a)
print(f"tuple_c元组的内容：{tuple_c}")



"""元组的常用操作
多少个元素
最大
最小
100的出现的次数
100第一次出现元组的索引(index)
300在这个元组中吗
 
"""
tuple_d=(100,7.1,200,12)
print(f"tuple_d元组的最大元素：{max(tuple_d)}")
