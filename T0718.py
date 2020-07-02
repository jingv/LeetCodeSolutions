#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0718.py
@Time    :   2020/07/01 13:12:00
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def findLength(self, A, B):
        m, n, result = len(A), len(B), 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                result = max(result, dp[i][j])
        return result


def main():
    tests = [
        [
            [1, 2, 3, 2, 1],
            [3, 2, 1, 4, 7],
        ],
    ]
    solution = Solution()
    for A, B in tests:
        print(solution.findLength(A, B))


if __name__ == "__main__":
    main()
