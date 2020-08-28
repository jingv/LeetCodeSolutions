#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SomeNode.py
@Time    :   2020/03/10 08:52:54
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class TreeNode():
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
