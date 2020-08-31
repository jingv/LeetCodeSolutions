#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0055.py
@Time    :   2020/04/17 10:13:48
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def canJump(self, nums:List[int]) -> bool
    def canJump(self, nums):
        # 递归 没问题但是超时 赣！
        result = True if len(nums) <= 1 else False
        for i in range(len(nums)-2, -1, -1):
            if(nums[i] >= len(nums) - i - 1):
                result = result or self.canJump(nums[:-1])
        return result

    def canJump2(self, nums):
        # 执行用时 :60 ms, 在所有 Python3 提交中击败了61.18%的用户
        # 内存消耗 :15.1 MB, 在所有 Python3 提交中击败了6.90%的用户
        # right_most 相当于可以到达的最远的下标的位置
        right_most = 0
        for i in range(len(nums)):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
            else:
                return False
            if right_most >= len(nums) - 1:
                return True
        return False


def main():
    tests = [
        # [],
        [0],
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4]
    ]
    solution = Solution()
    for test in tests:
        print("solution1: ", solution.canJump(test), " Solution2: ", solution.canJump2(test))


if __name__ == "__main__":
    main()
