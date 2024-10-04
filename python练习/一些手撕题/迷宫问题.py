#! /usr/bin/env python
# _*_ coding utf-8 _*_
# Date 括号的匹配问题

#用栈解决迷宫问题,深度优先搜索
import os
maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

# dirs=[
#     lambda x,y:(x+1,y),
#     lambda x,y:(x-1,y),
#     lambda x,y:(x,y+1),
#     lambda x,y:(x,y-1),
# ]
# def maze_path(x1,y1,x2,y2):
#     stack=[]
#     stack.append((x1,y1))
#     while(len(stack)>0):
#         curNode=stack[-1]#当前节点,cueNode是列表
#         if curNode[0]==x2 and curNode[0]==y2:#已经到终点
#             for p in stack:
#                 print(p)
#             return True
#         for dir in dirs:
#             nextNode=dir(curNode[0],curNode[1])
#             if maze[nextNode[0]][nextNode[1]]==0:
#                 stack.append(nextNode)
#                 maze[nextNode[0]][nextNode[1]]=2;#2表示已经走过
#                 break
#         else:
#             maze[nextNode[0]][nextNode[1]]=2
#             stack.pop()
#     else:
#         print('没有路')
#         return False

dirs=[
    lambda x,y:(x-1,y),
    lambda x,y:(x+1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
]
def maze_path(x_start,y_start,x_end,y_end):
    stack=[]
    stack.append((x_start,y_start))#起始位置进栈
    #走下一个点
    
    while(len(stack)!=0):
        CurNode=stack[-1]#CurNode[0]=x,CurNode[1]=y
        maze[x_start][y_start]=2
        if CurNode[0]==x_end and CurNode[1]==y_end:
            for p in stack:
                print(p)
            return True
        if(maze[CurNode[0]-1][CurNode[1]]==0):#上
            stack.append((CurNode[0]-1,CurNode[1]))
            maze[CurNode[0]-1][CurNode[1]]=2
            continue
        elif(maze[CurNode[0]+1][CurNode[1]]==0):#下
            stack.append((CurNode[0]+1,CurNode[1]))
            maze[CurNode[0]+1][CurNode[1]]=2
            continue
        elif(maze[CurNode[0]][CurNode[1]-1]==0):#左
            stack.append((CurNode[0],CurNode[1]-1))
            maze[CurNode[0]+1][CurNode[1]]=2
            continue
        elif(maze[CurNode[0]][CurNode[1]+1]==0):#右
            stack.append((CurNode[0],CurNode[1]+1))
            maze[CurNode[0]][CurNode[1]+1]=2
            continue        
        else:
            stack.pop()
            continue 
    print("没有路")
    return False





print(maze_path(1,1,8,8))


        