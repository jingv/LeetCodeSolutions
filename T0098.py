#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0098.py
@Time    :   2020/05/05 08:32:24
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''

# 逻辑存在漏洞，无法断定右子树满足中左侧元素小于根节点的情况是否满足要求！！！
# BST概念待补充


class Solution():
    def isValidBST(self, root):
        if root is None:
            return True
        if ((not root.left) or (root.left.element is not None and root.left.element < root.element)) and ((not root.right) or (root.right.element is not None and root.right.element > root.element)):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        return False


def main():
    solution = Solution()

    from Constructor.BinaryTree import BinaryTree

    tests = [
        [2, 1, 3],
        [5, 1, 4, None, None, 3, 6],
        [1, None, 1],
        [10, 5, 15, None, None, 6, 20],
    ]

    for test in tests:
        tree = BinaryTree()
        for item in test:
            tree.add(item)
        tree.breadth_trval()
        print()
        print(solution.isValidBST(tree.root))


if __name__ == "__main__":
    main()
