#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0062.py
@Time    :   2020/03/30 13:04:31
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''

import sys

sys.setrecursionlimit(100000)


class Solution:
    def cal_result(self, n, m):
        if n == 0:
            return 0
        x = self.cal_result(n - 1, m)
        return (m + x) % n

    def cal_result2(self, nums, m):
        while len(nums) > 1:
            index = m % len(nums) if m > len(nums) else m
            nums = nums[index:] + nums[:index - 1]
        return nums[0]

    def lastRemaining(self, n, m):
        # return self.cal_result(n, m)
        return self.cal_result2(list(range(n)), m)


def main():
    tests = [
        (5, 3),
        (10, 17),
        (88, 10)
    ]
    solution = Solution()
    for n, m in tests:
        print(solution.lastRemaining(n, m))


if __name__ == "__main__":
    main()
