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

