#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
# 栈
# 先进后出，装网球那样
class Stack(object):
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self, x):
        if self.isfull():
            raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top += 1

    def pop(self):
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            self.stack.pop()

    def isfull(self):
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == -1

    def showStack(self):
        print(self.stack)

s = Stack(10)
for i in range(5):
    s.push(i)

s.showStack()
for i in range(3):
    s.pop()

s.showStack()