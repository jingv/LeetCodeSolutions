#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0543.py
@Time    :   2020/03/10 09:01:53
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''
from Constructor.BinaryTree import BinaryTree


class Solution:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    # def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.ans = max(self.ans, left_depth+right_depth+1)
            # 返回该节点为根的子树的深度
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.ans - 1


def main():
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)
    solution = Solution()
    print(solution.diameterOfBinaryTree(tree))
    pass


if __name__ == "__main__":
    main()
