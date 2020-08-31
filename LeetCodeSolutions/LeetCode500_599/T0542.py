#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0542.py
@Time    :   2020/04/15 08:49:41
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def updateMatrix(self, matrix):
        # 动态规划
        # 原则上是左上、左下、右上、右下四个方向移动；
        # 左上与右下（或者说右上和左下）就可以包含四个方向的移动，所以只需要保留两组中的一组即可
        # 执行用时 :744 ms, 在所有 Python3 提交中击败了69.95%的用户
        # 内存消耗 :16.5 MB, 在所有 Python3 提交中击败了100.00%的用户
        m, n = len(matrix), len(matrix[0])
        result = [[10**9] * n for _ in range(m)]
        # 如果当前元素为0， 则距离为0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    result[i][j] = 0
        # 左上移动
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    result[i][j] = min(result[i][j], result[i - 1][j] + 1)
                if j - 1 >= 0:
                    result[i][j] = min(result[i][j], result[i][j - 1] + 1)
        # 右下移动
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    result[i][j] = min(result[i][j], result[i + 1][j] + 1)
                if j + 1 < n:
                    result[i][j] = min(result[i][j], result[i][j + 1] + 1)
        return result


def main():
    tests = [
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ],
    ]
    solution = Solution()
    for test in tests:
        print(solution.updateMatrix(test))


if __name__ == "__main__":
    main()
