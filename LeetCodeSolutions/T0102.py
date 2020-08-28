#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0102.py
@Time    :   2020/05/13 08:30:04
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''

from Constructor.BinaryTree import BinaryTree as Tree


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result, level_temp = [], []
        nodes = [root, "level"]
        while nodes:
            temp = nodes.pop(0)
            if temp == "level":
                result.append(level_temp)
                level_temp = []
                if nodes:
                    nodes.append("level")
                    continue
                else:
                    break
            if temp.element is not None:
                level_temp.append(temp.element)
            if temp.left is not None:
                nodes.append(temp.left)
            if temp.right is not None:
                nodes.append(temp.right)
        return result


def main():
    tests = [
        [3, 9, 20, None, None, 15, 17],
        [],
        [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8]
    ]
    solution = Solution()
    for test in tests:
        tree = Tree()
        for node in test:
            tree.add(node)
        tree.breadth_trval()
        print()
        print(solution.levelOrder(tree.root))


if __name__ == "__main__":
    main()
