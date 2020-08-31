#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0010.py
@Time    :   2020/07/21 17:29:23
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def isMath(self, s, p):

        def matches(i, j):
            if i == 0:
                return False
            elif p[j - 1] == ".":
                return True
            else:
                return s[i - 1] == p[j - 1]

        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]
                    if matches(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]


def main():
    solution = Solution()
    tests = [
        ["zz", "z"],
        ["thissssssssssssssaaaaaa", "this*a*a"]
    ]
    for s, p in tests:
        print(solution.isMath(s, p))


if __name__ == "__main__":
    main()
