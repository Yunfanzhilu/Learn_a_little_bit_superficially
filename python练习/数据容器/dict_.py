
"""
列表   可修改            可重复
元组   不可修改           可重复
集合   支持部分可修改      不可重复
字典   key不可重复 value可重复
"""

"""
字典存储的元素是：键值对
键可以是任何不可变类型，字符串和数字总是可以作为键，Value可以是任意数据类型
"""
from numpy.core.defchararray import upper

dict_tes={'TOP':369,'jungle':"tian",'mid':"cream","ADC":"jackeylove",'support':"meiko"}
print("dict_tes_adc:",{dict_tes["ADC"]})

dict_a={"jack_list":[100,20],
        "jack_tuple":(100,2.3,"apple"),
        "jack_set":{"100",3.7},
        "jack_dict":{"jack_dict_sub":12}
        }
print(f"dict:{dict_a},类型：{type(dict_a)}")

"""
字典不支持索引
字典遍历
1.依次取出key
2.依次取出value
3.依次取出key-value
"""
for key in dict_tes:
    print(f"key:{key},{dict_tes[key]}")

for value in dict_tes:
    print(f"value:{value}")

for k,v in dict_tes.items():
    print(f"key:{k},value:{v}")



"""
字典常用操作
1.返回字典的项数
2.返回以key为键的项，如果映射中不存在key，则会引发keyError
3.修改value
4.添加key
5.删除key
6.pop(key) 返回dict[key]并移除
7.返回字典所有key   keys()
8.判断字典是否有key
"""


"""
字典生成式

"""
Loc=["TOP","JUN","MID","BOT","SUP"]
Per=["flandre","karsa","cool","ruler","meiko"]

Team_huang={Loc:Per.upper() for Loc,Per in zip(Loc,Per)}
print(Team_huang)

print('-----字典-------')
dict01 = {'乔治': 87, '恩比德': 92, '约基奇': 96, '勒布朗': 96}

print('-----获取字典-------')
print(dict01['乔治'])
print(dict01.get("乔治"))

print('-----key的判断-------')
print('勒布朗' in dict01)
del dict01['乔治']
print(dict01)
dict01['库里'] = 97
print(dict01)

print('-----获取所有的key------')
keys = dict01.keys()
print(keys)
print(type(keys))
print(list(keys))

print('-----获取所有的values------')
values = dict01.values()
print(values)
print(type(values))
print(list(values))

print('-----获取所有的keys-values------')
items = dict01.items()
print(items)
print(list(items))  # 元组

print('------字典元素的遍历-------')
for item in dict01:
    print(item, dict01[item], dict01.get(item))
print('hello,world')

print('------字典生成式------')
items = ['德布劳内', '哈兰德', '凯恩']
prices = [97, 97, 94]
d = {item: price for item, price in zip(items, prices)}
print(d)





