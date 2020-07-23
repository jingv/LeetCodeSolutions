#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0064.py
@Time    :   2020/07/23 09:34:48
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def minPathSum(self, grid):
        # 第一行只能向右移: dp[0][i] = dp[0][i-1]
        # 第一列只能向下移: dp[i][0] = dp[i-1][0]
        # 其余向右或向下移: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # 初始: dp[0][0] = grid[0][0]
        if not grid or not grid[0]:
            return 0

        # 执行用时：56 ms, 在所有 Python3 提交中击败了82.39%的用户
        # 内存消耗：15.2 MB, 在所有 Python3 提交中击败了8.33%的用户
        row, colum = len(grid), len(grid[0])
        result = [[0 for _ in range(colum)] for _ in range(row)]
        for i in range(row):
            for j in range(colum):
                if i == 0:
                    # 如果i == 0, j == 0, 即dp[0][0] = grid[0][0]
                    # 这时候result[0][0] = result[0][-1] + grid[0][0]
                    # 因为result[0][-1] == 0, 刚好可以满足动态转移方程。没料到，运气！
                    result[i][j] = result[i][j - 1] + grid[i][j]
                    continue
                if j == 0:
                    result[i][j] = result[i - 1][j] + grid[i][j]
                    continue
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]
        return result[-1][-1]

    # 空间优化, 在原有数组的基础上进行修改, 优化了个锤锤！还不如上一个！
    def minPathSum2(self, grid):
        if not grid or not grid[0]:
            return 0

        row, colum = len(grid), len(grid[0])
        for i in range(row):
            for j in range(colum):
                temp = grid[i][j]
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j - 1] + temp
                    continue
                if j == 0:
                    grid[i][j] = grid[i - 1][j] + temp
                    continue
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + temp
        return grid[-1][-1]


def main():
    solution = Solution()
    tests = [
        # [[1]],
        # [
        #     [1, 3, 1],
        #     [1, 5, 1],
        #     [4, 2, 1]
        # ],
        [
            [1, 2],
            [5, 6],
            [1, 1],
        ]

    ]
    for test in tests:
        print("result of minPathSum is {}, result of minPathSum2 is {}".format(solution.minPathSum(test), solution.minPathSum2(test)))


if __name__ == "__main__":
    main()
