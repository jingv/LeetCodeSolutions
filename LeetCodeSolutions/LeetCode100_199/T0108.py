#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0108.py
@Time    :   2020/07/03 08:50:21
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''

from Constructor.SomeNode import TreeNode


class Solution():
    def sortedArrayToBST(self, nums):

        def build(nums):
            if not nums:
                return
            mid = len(nums) // 2
            # print("mid = {mid}, nums = {nums}".format(mid=mid, nums=nums))
            tree = TreeNode(nums[mid])
            tree.left = build(nums[:mid])
            tree.right = build(nums[mid + 1:])

            return tree

        return build(nums)


def preorder_travel(node):
    if node is None:
        return
    print(node.element, end=" ")
    preorder_travel(node.left)
    preorder_travel(node.right)


def main():
    tests = [
        [-10, -3, 0, 5, 9],
    ]
    solution = Solution()
    for test in tests:
        tree = solution.sortedArrayToBST(test)
        preorder_travel(tree)


if __name__ == "__main__":
    main()
