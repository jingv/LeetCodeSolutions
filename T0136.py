#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0136.py
@Time    :   2020/05/14 08:38:30
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result


def main():
    tests = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
    ]
    solution = Solution()
    for test in tests:
        print(solution.singleNumber(test))


if __name__ == "__main__":
    main()
