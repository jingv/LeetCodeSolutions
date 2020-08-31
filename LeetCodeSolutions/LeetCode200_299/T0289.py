#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0289.py
@Time    :   2020/04/02 08:54:30
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def gameOfLife(self, board: List[List[int]]) -> None:
    def gameOfLife(self, board):
        # live => death : -1
        # death => live : 2
        pass

    def gameOfLife2(self, board):
        # 卷积
        # 执行用时 :120 ms, 在所有 Python3 提交中击败了5.04%的用户
        # 内存消耗 :29.2 MB, 在所有 Python3 提交中击败了10.53%的用户
        import numpy as np
        r, c = len(board), len(board[0])
        # 用0填充数组
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        board_exp[1:1+r, 1:1+c] = np.array(board)
        # 设置内核
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        # 开始卷积
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 统计细胞周围8个位置的状态
                temp_sum = np.sum(kernel*board_exp[i - 1: i + 2, j - 1: j + 2])
                # 如果当前细胞为活着的状态
                if board_exp[i, j] == 1:
                    # 细胞死亡的情况
                    if not 2 <= temp_sum <= 3:
                        board[i-1][j-1] = 0
                else:
                    # 细胞复活的条件
                    if temp_sum == 3:
                        board[i-1][j-1] = 1
        return board


def main():
    tests = [
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
    ]
    solution = Solution()
    for test in tests:
        print(solution.gameOfLife2(test))


if __name__ == "__main__":
    main()
