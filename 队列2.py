#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # 和第一种完全不同的地方是这个方法更加聪明。直接把后面添加的放到第一位，
    # 这样就把之前的挤到后面去了，
    # 再pop的时候直接pop最后面的那位就保证了先进先出的原则
    def enqueue(self, item):
        """进队列"""
        self.items.insert(0, item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

    def show_queue(self):
        return self.items

if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.show_queue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())