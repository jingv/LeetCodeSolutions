#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0199.py
@Time    :   2020/04/22 08:38:02
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''
from Constructor import BinaryTree


class Solution:
    def rightSideView(self, root):
        # 官方解答
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]      


def main():
    tests = [[1, 2, 3, None, 5, None, 4]]
    binary_tree = BinaryTree.BinaryTree()
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(None)
    binary_tree.add(5)
    binary_tree.add(None)
    binary_tree.add(4)
    # binary_tree.breadth_trval()

    solution = Solution()
    for test in tests:
        print(solution.rightSideView(test))


if __name__ == "__main__":
    main()
