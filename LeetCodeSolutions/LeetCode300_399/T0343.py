#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0343.py
@Time    :   2020/07/30 13:05:20
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def interBreak(self, n):
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


def main():
    solution = Solution()
    tests = [2, 10]
    for test in tests:
        print(solution.interBreak(test))


if __name__ == "__main__":
    main()
