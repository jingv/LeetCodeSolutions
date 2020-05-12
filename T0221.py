#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0221.py
@Time    :   2020/05/08 09:26:45
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def maximalSquare(self, matrix):
        import numpy as np
        board = np.array(matrix)
        width = min(len(matrix), len(matrix[0]))
        for square_width in range(width, 0, -1):
            # 设置内核
            kernel = [[1 for _ in range(square_width)] for _ in range(square_width)]
            # 开始卷积
            for i in range(0, len(matrix) - square_width + 1):
                for j in range(0, len(matrix[0]) - square_width + 1):
                    # 矩形框中1的数量
                    temp_sum = np.sum(kernel * board[i: i + square_width, j: j + square_width])
                    if(temp_sum == square_width ** 2):
                        return temp_sum
        return 0


def main():
    tests = [
        [[1]],
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
    ]
    solution = Solution()
    for test in tests:
        print(solution.maximalSquare(test))


if __name__ == "__main__":
    main()
