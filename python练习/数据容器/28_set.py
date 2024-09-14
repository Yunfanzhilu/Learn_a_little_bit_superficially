"""
1.python 支持集合  集合是由「」组成的「」容器？
2.集合对象支持「」「」「」等数学运算？
3.既然有列表、元组这些数据容器，为什么还需要提供集合？

回顾：列表、元组的元素是可以「」并且「」？
"""
set_a = {100, 200, 300, 300}
basket = {'apple', 'banana', 'orange', 'apple', 'banana'}
print(f"set_a的内容：{set_a},类型是：{type(set_a)}")
print(f"basket：{basket},类型是：{type(basket)}")

"""
4.集合支持索引吗？
"""
# print(set_a[0])

"""
5.集合的遍历 while和for都可以吗？
"""
for ele in basket:
    print(f"正在使用for循环输出集合basket的元素：{ele}")

"""
6.创建空集合怎么做?
"""
set_null = {}
set_none = set()
print(f"set_null的内容：{set_null},set_null的类型：{type(set_null)}")
print(f"set_none的内容：{set_none},set_none的类型：{type(set_none)}")

"""
7.集合的常用功能
"""
# 统计集合的个数？


# 判断apple是否在集合中？

# 将grape加入到集合中(add)


# 移除某个元素(remove)

# 并集  union   |

# 交集 intersection    &

# 差集 difference   difference  -


"""
8.集合生成式
"""

set_create_1 = {ele * 2 for ele in range(1, 8)}
print(f"集合生成式set_create_1:{set_create_1}")

set_create_2 = {ele + ele for ele in "斯蒂芬库里"}
print(f"集合生成式set_create_2:{set_create_2}")

"""
1.用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)
求选课学生总共多少人？
求只选了第一个学科(history的学生数量和学生名字)
求只选了一门学科的学生数量和学生名字
求选了三门学科的学生数量和学生名字

"""
s_history = {"小明", "张三", "李四", "王五", "Lily", "Bob", "grace"}
s_politic = {"小明", "小花", "小红", "二狗", "grace"}
s_english = {"小明", "Lily", "Bob", "grace"}

print(f"选课学生一共有：{len(s_history | s_politic | s_english)}")

print(f"只选了第一个学科(history的学生数量)：{len(s_history - s_politic - s_english)}")
OnlyHistory = s_history - s_politic - s_english
for ele in OnlyHistory:
    print(f"只选了第一门学科的学生名字：{ele}")

#求只选了一门学科
s1=s_history - s_politic - s_english
s2=s_politic - s_english-s_history
s3=s_english - s_politic - s_history
OnlyOneSubject=s1 | s2 |s3
print(f"只选择一门学科的学生：{len(OnlyOneSubject)}")
for ele in OnlyOneSubject:
    print(f"只选择一门学科的学生名字：{ele}")

AllSubject = s_history & s_english & s_politic
print(f"选了三门学科的学生数量:{AllSubject}")
for ele in AllSubject:
    print(f"选择三门学科的学生名字：{ele}")


"""
关于排序
在Python中，你可以使用sorted()函数对集合进行排序。这是一个例子：
请注意，集合（set）在Python中是无序的数据结构，但你可以通过转换成列表（list）来对元素进行排序。sorted()函数会返回一个新的列表，而不是修改原始集合。
如果你想保持集合的无序性质，可以只查看排序后的列表。
"""
# 定义一个集合
my_set = {1, 16, 9, 4}

# 对集合进行排序
sorted_set = sorted(my_set)

# 打印排序后的集合
print(sorted_set)

set123={"jack1","jack21"}
print(set123)