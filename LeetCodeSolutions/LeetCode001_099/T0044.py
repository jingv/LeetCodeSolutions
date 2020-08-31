#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0044.py
@Time    :   2020/07/07 10:01:39
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def isMatch(self, s, p):
        # 动态规划， dp[i][j]表示s[i]与p[j]是否匹配的情况
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 如果Pj是星号，那么同样对Sj没有任何要求，
                    # 但是星号可以匹配零或任意多个小写字母，因此状态转移方程分为两种情况，即使用或不使用这个星号
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # 如果Pj是问号，那么对Sj没有任何要求
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


def main():
    solution = Solution()
    tests = [
        # ["aa", "a"],
        # ["aa", "*"],
        # ["Aaaaa*bbaba", "A*ab*"],
        ["aaa", "????"]
    ]
    for s, p in tests:
        print(solution.isMatch(s, p))


if __name__ == "__main__":
    main()
