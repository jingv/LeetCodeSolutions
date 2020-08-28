#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0112.py
@Time    :   2020/07/07 08:50:17
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


from Constructor.BinaryTree import BinaryTree


class Solution:
    def hasPathSum(self, root, sum):
        # 递归！
        if not root and sum != 0:
            return False

        return False or self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    
    def hasPathSumLOOP(self, root, sum):
        if not root:
            return False
        node_queue = [root]
        sum_queue = [root.val]
        while node_queue:
            node = node_queue.pop(0)
            item_sum = sum_queue.pop(0)
            # 如果当前节点为叶子节点，不再入队
            if not node.left and not node.right:
                if item_sum == sum:
                    return True
                continue
            if node.left:
                node_queue.append(node.left)
                sum_queue.append(item_sum + node.left.val)
            if node.right:
                node_queue.append(node.right)
                sum_queue.append(item_sum + node.right.val)
        return False


def main():
    solution = Solution()
    binary_tree = BinaryTree()
    tree_val = [5, 4, 8, 11, 13, 4, 7, 2, None, 1]
    for val in tree_val:
        binary_tree.add(val)
    tests = [
        (binary_tree, 22)
    ]
    for tree, s in tests:
        print(solution.hasPathSum(tree, s))


if __name__ == "__main__":
    main()
