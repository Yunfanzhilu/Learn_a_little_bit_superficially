#! /usr/bin/env python
# _*_ coding utf-8 _*_
# Date 
# 二叉树
from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("Ea")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.left = a
e.right = g
a.right = c
g.right = f
c.left = b
c.right = d


# Consolas, 'Courier New', monospace

# 前序遍历
# def pre_order(root):
#     if root:
#         print(root.data,end=",")
#         pre_order(root.left)
#         pre_order(root.right)
def pre_order(root):
    if root == None:
        return 1
    print(root.data, end=",")
    pre_order(root.left)
    pre_order(root.right)


# def pre_order_pro2(root):
#     print("非递归方式打印先序遍历：")
#     stack_s1=[]
#     stack_s1.append(root.data)
#     while(len(stack_s1)!=0):
#         print(stack_s1[-1])
#         root=stack_s1.pop()
#         if root.left:
#             stack_s1.append(root.left.data)
#         if root.right:
#             stack_s1.append(root.right.data)


# 中序遍历
def mid_order(root):
    if root:
        mid_order(root.left)
        print(root.data, end=",")
        mid_order(root.right)


# 后序遍历
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=",")


# 层次遍历
def level_order(root):
    queue_q1 = deque()
    queue_q1.append(root)
    while len(queue_q1) > 0:
        node = queue_q1.popleft()
        print(node.data, end=",")
        if node.left:
            queue_q1.append(node.left)
        if node.right:
            queue_q1.append(node.right)


pre_order(e)
print("\n")
mid_order(e)
print("\n")
post_order(e)
print("\n")
level_order(e)
print("\n")
# pre_order_pro2(e)
