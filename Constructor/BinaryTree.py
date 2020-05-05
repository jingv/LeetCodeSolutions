#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   BinaryTree.py
@Time    :   2020/03/10 08:36:03
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''
from .SomeNode import TreeNode as Node


class BinaryTree():
    def __init__(self):
        self.root = None

    def add(self, element):
        node = Node(element)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left is None:
                cur.left = node
                return
            else:
                queue.append(cur.left)
            if cur.right is None:
                cur.right = node
                return
            else:
                queue.append(cur.right)

    def breadth_trval(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.element, end=' ')
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.element, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.left)
        print(node.element, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.element, end=" ")


def main():
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)
    tree.breadth_trval()
    print('')
    tree.preorder(tree.root)
    print('')
    tree.inorder(tree.root)
    print('')
    tree.postorder(tree.root)
    print('')


if __name__ == '__main__':
    main()
