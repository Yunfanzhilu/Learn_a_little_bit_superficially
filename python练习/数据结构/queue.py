#! /usr/bin/env python
# _*_ coding utf-8 _*_
# Date 队列

class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 对首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            self.queue.pop()
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty')

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
for i in range(2):
    q.push(i)
q.push(7)
q.push(18)

#for i in range(q.size):
 #   print(q[i])
a=[1,27,3]
print("这里:",a[1])
# fastdfs:
#   nginx:
#     #host: http://192.168.91.128/
