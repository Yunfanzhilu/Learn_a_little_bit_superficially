#! /usr/bin/env python
# _*_ coding utf-8 _*_
# Date 
# 各类排序

# 冒泡i排序
li = [6, 2, 1, 9, 31, 11, 5.1, 4.1, 1.2]


def bubble_sort(li):
    for i in range(len(li)):
        j = i + 1
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)


bubble_sort(li)
print(li)


# 快速排序

def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


quick_sort(li, 0, len(li) - 1)
print(li)
