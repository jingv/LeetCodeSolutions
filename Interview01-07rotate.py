#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview01-07rotate.py
@Time    :   2020/04/07 19:53:29
@Author  :   JingV
@Version :   1.0
@Contact :   dllOoOllb.com
@Desc    :   None
'''


class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    def rotate(self, matrix):
        # 先将数组上下翻转，再将数组按照对角线反转即可得到结果
        # 执行用时 :48 ms, 在所有Python3 提交中击败了28.83%的用户
        # 内存消耗 :13.7 MB, 在所有Python3 提交中击败了100.00%的用户
        for i in range(len(matrix)//2):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[len(matrix) - 1 - i][j] = matrix[len(matrix) - 1 - i][j], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


def main():
    tests = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ],
        [],
    ]
    solution = Solution()
    for test in tests:
        print(solution.rotate(test))


if __name__ == "__main__":
    main()
