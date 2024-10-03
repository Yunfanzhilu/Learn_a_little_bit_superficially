
"""
列表   可修改            可重复
元组   不可修改           可重复
集合   支持部分可修改      不可重复
字典   key不可重复 value可重复
"""
"""
字符串是不可变序列
"""

"""字符串常用方法"""


"""切片,操作不影响原序列，而是返回一个新的序列
[起始索引：结束索引)
"""
str1="hello world!"
print(f"str_slice:{str1[0:5:1]}")

str2=["jack","Bob","candy","chovy","keria"]
blg=["bin","xun","knight","elk","on"]
print(f"正向取str2_slice:{str2[0::3]}")
print(f"反向取blg_slice:{blg[-1:-len(blg):-3]}，blg:{blg}")
print(f"取出blg前三个名字：{blg[0:3:1]},取出blg后三个名字:{blg[-3::1]}")

print('------字符串驻留机制--------')
a = 'lebron'
b = "lebron"
c = """lebron"""
print(a, id(a))
print(b, id(b))
print(c, id(c))
'''python中字符串是基本数据类型，不可变字符序列
字符串驻留机制
'''

print('------字符串查询--------')
s = 'hello,world'
print(s.find('el'))
print(s.rfind('ld'))

print('------字符串大小写--------')
s2 = 'curry'
print(s2.lower())
print(s2.upper())

print('------字符串填充对齐操作--------')
s3 = 'hello,python'
print('s3的长度:', len(s3))
print(s3.center(30, '*'))
# 左对齐
print(s3.ljust(20, '*'))
print(s3.ljust(20))
# 右对齐
print(s3.rjust(20, '*'))
print(s3.rjust(20))
print(s3.rjust(10))

print('------字符串合法判断-------')
# 合法的标识符：1、不能以数字开头；2、不能包含非法字符；3、数字不能作为标识符；4、不能包含空格；5、不能包含运算符。所以说张三合法
# 中文的汉字会被python判定成字母，想区分中英文可使用unicode，中文的范围为：['/u4e00'，'/u9fa5']
# 想区分中英文可以这么写‘张三1’.encode('UTF-8').isalpha()
print("字符串合法判断1", '你好'.isidentifier())
print("字符串合法判断2", '1_2'.isidentifier())
print("字符串合法判断3", '_2'.isidentifier())

print('------字符串替换合并方式--------')
s4 = 'hello,Python'
print(s4.replace('Python', 'Java'))
s5 = 'hello,Python,Python,Python'
print(s5.replace('Python', 'C++', 2))

lst = ['hello', 'java', 'python']
print(','.join(lst))
print('+'.join(lst))

