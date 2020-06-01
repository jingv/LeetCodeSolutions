#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0053.py
@Time    :   2020/05/03 10:53:13
@Author  :   JingV
@Version :   1.0
@Contact :   dllOoOllb.com
@Desc    :   None
'''


class Solution():
    def maxSubArray(self, nums):
        if not nums:
            return 0
        pre_result, result = 0, nums[0]
        for i in nums:
            pre_result = max(pre_result + i, i)
            result = max(result, pre_result)
        return result


def main():
    tests = [
        [],
        [1],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    ]
    solution = Solution()
    for test in tests:
        print(solution.maxSubArray(test))


if __name__ == "__main__":
    main()
