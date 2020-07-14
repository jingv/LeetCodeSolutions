#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0120.py
@Time    :   2020/07/14 09:08:36
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def minimumTotal(self, triangle):
        # 动态规划 经典！~
        n = len(triangle)
        f = [[0 for _ in range(n)] for _ in range(n)]
        # print(f)
        f[0][0] = triangle[0][0]
        # i 为当前的行数
        for i in range(1, n):
            # 当我们在第i行最左侧时，只能从第i-1行的最左侧移动过来
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                # 要走到位置(i, j)上，上一步只能在位置(i-1, j-1)或(i-1, j)。
                # 在两个位置中选择一个路径和较小的来进行转移
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            # 当我们在第i行最右侧时，只能从第i-1行的最右侧移动过来
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])
        # 进一步优化1：状态转换只与上一个状态有关系，所以只存储上一个状态得到的结果即可。
        # 进一步优化2：倒序遍历每一个元素，这样前面元素都是用到的上一个状态的结果


def main():
    solution = Solution()
    tests = [
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ],
    ]
    for test in tests:
        print(solution.minimumTotal(test))


if __name__ == "__main__":
    main()
