#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0155.py
@Time    :   2020/05/12 08:41:20
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
        self.stack.append(x)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None


def main():
    minStack = MinStack()
    num_li = [-2, 0, -3]
    for num in num_li:
        minStack.push(num)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())


if __name__ == "__main__":
    main()
