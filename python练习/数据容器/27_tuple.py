
"""
列表   可修改            可重复
元组   不可修改           可重复
集合   支持部分可修改      不可重复
字典   key不可重复 value可重复
"""

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

print('------元组的建立------')
t = ('python', 'world', 98)
print("元组的建立,直接创建", t)
print(type(t))
t3 = ('python')  # 如果元组中只有一个元素，小括号不能省略
t4 = tuple(('qwe', 123))
print("元组的建立，使用内置函数tuple", t4)
# 为什么将字符串和元组设计成不可变序列(没有增删改操作),集合列表字典是可变序列
# 在多任务环境下，同时操作对象时不需要加锁
# 因此，在程序中尽量使用不可变序列
# 举例
t_example = (10, [20, 30], 40)
print(t_example)
print(t_example[1], id(t_example[1]))
t_example[1].append(60)
print(t_example[1], id(t_example[1]))

print('------元组的遍历------')
t_traverse = ('python', 'java', 97)
for i in t_traverse:
    print(i)