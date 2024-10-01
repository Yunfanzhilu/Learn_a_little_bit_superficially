
"""
列表   可修改            可重复
元组   不可修改           可重复
集合   支持部分可修改      不可重复
字典   key不可重复 value可重复
"""
list1 = [10, 60, 30]
list2 = [10, 40, "五十", '六十', 70]

print('-----列表遍历-----')
for i in list2:
    print("列表遍历", i)

print('-----列表排序-----')
list1.sort()
print('排序后的列表,默认升序', list1, id(list1))
# 指定关键字参数，将列表中的元素进行降序排序
list1.sort(reverse=True)
print(list1)

print('-----------使用内置函数sorted()对列表进行排序，将产生一个新的额列表对象-------------')
list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('原列表', list3)
new_list3 = sorted(list3)
print('新的列表', new_list3)
# 指定关键字参数，实现列表元素的降序排序
desc_list3 = sorted(list3, reverse=True)
print('新的降序列表', desc_list3)

print('-----列表指定索引-----')
list6 = [10, 90, 30, 709, 89, 92]
print('获取索引为0的元素', list6[0])
print('获取索引为-1的元素', list6[-1])

print('-----列表指定切片 [begin:end:step)-----,默认步长1')
print('列表指定切片', list3[0:9:2])
print('列表指定切片，步长为负数', list3[::-2])

print('-----列表添加删除修改-----')
list3.append(110)
print("列表添加append", list3)
list3.insert(2, 220)
print("列表添加insert", list3)
list3.remove(220)
print("列表删除remove", list3)
list3.pop()
print("列表删除pop", list3)
list3.pop(len(list3) - 3)  # java track.remove(track.size()-1);
print("列表删除pop", list3)
list3[1] = 330
print("列表修改", list3)

print('-----列表生成式-----')
list4 = [i * 1 for i in range(1, 9)]
print("列表生成式 list4=", list4)