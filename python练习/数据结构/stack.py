#! /usr/bin/env python
# _*_ coding utf-8 _*_
# Date 用列表实现栈

# 用列表实现栈
# class Stack:

#     def __init__(self):#构造函数
#          self.stack=[]
#     def push(self,element):
#         self.stack.append(element)
#     def pop(self):
#         return self.stack.pop()

#     def get_top(self):
#         if len(self.stack)>0:
#             return self.stack[-1]
#         else:
#             return None
#     def is_empty(self):
#         return len(self.stack)==0



class Stack():
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
        print("栈内新增元素：",element)
    def pop(self):
        if len(self.stack)==0:
            print("栈为空")
        else:
            temp=self.stack[-1]
            self.stack.pop()
            print("删除栈顶元素：",temp)
    def gettop(self):
        if len(self.stack)==0:
            print("栈为空")
        else:
            return self.stack[-1]
           








stack_s1=Stack()
stack_s1.push(1)
stack_s1.push(2)
stack_s1.push(3)
stack_s1.push(7)
print(stack_s1.gettop())
