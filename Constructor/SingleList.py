#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SingleList.py
@Time    :   2020/07/03 09:31:15
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''

from .SomeNode import ListNode


class SingleList():
    def __init__(self):
        self.head = None
        self.__cur = self.head

    def Add(self, item):
        node = ListNode(item)
        if not self.head:
            self.head = node
            self.__cur = self.head.next
        else:
            self.__cur = node
            self.__cur = self.__cur.next


def Travel(list_node):
    cur = list_node
    while cur:
        print(cur.val, end=" ")
        cur = cur.next


if __name__ == "__main__":
    single_list = SingleList()
    for i in range(1, 6):
        single_list.Add(i)
    Travel(single_list.head)
