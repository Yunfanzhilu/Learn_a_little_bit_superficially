import os
#! /usr/bin/env python
# _*_ coding utf-8 _*_
# Date 括号的匹配问题
class Stack:

    def __init__(self):
         self.stack=[]
    def push(self,element):

        self.stack.append(element)
    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack)==0



# def brace_match(s):
#     dict_match={'}':'{',']':'[',')':'('}
#     stack_s1=Stack()
#     for ch in s:
#         if ch in{'(','[','{'}:
#             stack_s1.push(ch)
#         else:
#             if stack_s1.is_empty():
#                 return False
#             elif stack_s1.get_top()==dict_match[ch]:
#                 stack_s1.pop()
#             else:
#                 return False
#     if stack_s1.is_empty():
#         return True
#     else:
#         return False

# def brace_match(str):
#     dict_brace_match={'}':'{',']':'[',')':'('}
#     stack_s1=Stack()
#     for ch in str:
#         if ch in{'{','[','('}:
#             stack_s1.push(ch)
#         else:
#             if stack_s1.is_empty():
#                 return False
#             elif stack_s1.get_top()==dict_brace_match[ch]:
#                 stack_s1.pop()
#             else:
#                 return False
#     if stack_s1.is_empty():
#         return True
#     else:
#         return False
                
            
def brace_match(s):
    dict_brace={')':'(','}':'{',']':'['}
    stack_s1=Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack_s1.push(ch)
        else:
            if stack_s1.is_empty():
                return False
            elif stack_s1.get_top()==dict_brace[ch]:
                return True
            else:
                return False
                

print(brace_match('(())[()][{}]{}'))


         