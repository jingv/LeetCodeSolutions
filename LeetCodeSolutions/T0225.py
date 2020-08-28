#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0225.py
@Time    :   2020/07/07 11:08:53
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue_a = []
        self.__queue_b = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.__queue_a:
            self.__queue_a.append(x)
            while self.__queue_b:
                self.__queue_a.append(self.__queue_b.pop(0))
        else:
            self.__queue_b.append(x)
            while self.__queue_a:
                self.__queue_b.append(self.__queue_a.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.__queue_a:
            return self.__queue_a.pop(0)
        elif self.__queue_b:
            return self.__queue_b.pop(0)
        return None

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.__queue_a:
            return self.__queue_a[0]
        elif self.__queue_b:
            return self.__queue_b[0]
        return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.__queue_a and not self.__queue_b


if __name__ == "__main__":
    test = MyStack()
    test.push(1)
    test.push(2)
    print(test.top())
    print(test.pop())
    print(test.top())
    print(test.empty())
    print(test.pop())
    print(test.empty())
