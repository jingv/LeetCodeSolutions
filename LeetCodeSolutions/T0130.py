#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0130.py
@Time    :   2020/08/11 09:00:57
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def solve(self, board):
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        row, colum = len(board), len(board[0])
        except_o = []
        # 先将边界的O加入到列表中
        for i in [0, row - 1]:
            for j in range(colum):
                if board[i][j] == "O" and (i, j) not in except_o:
                    except_o.append((i, j))
        for i in [0, colum - 1]:
            for j in range(row):
                if board[j][i] == 'O' and (j, i) not in except_o:
                    except_o.append((j, i))
        print(except_o)
        # 遍历边界上的O，将相邻的O添加到列表中
        around = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for pos_r, pos_c in except_o:
            for r, c in around:
                temp_r, temp_c = pos_r + r, pos_c + c
                if 0 <= temp_c <= colum - 1 and 0 <= temp_r <= row - 1:
                    if board[temp_r][temp_c] == 'O' and (temp_r, temp_c) not in except_o:
                        except_o.append((temp_r, temp_c))
        # print(except_o)
        for i in range(row):
            for j in range(colum):
                if board[i][j] == 'O' and (i, j) not in except_o:
                    board[i][j] = 'X'


def main():
    solution = Solution()
    tests = [
        [],
        [[]],
        [
            ['X', 'O', 'X', 'X'],
        ],
        [
            ['X'],
            ['O'],
            ['X'],
            ['X'],
        ],
        [
            ['X', 'X', 'X'],
            ['X', 'O', 'X'],
            ['X', 'X', 'X'],
        ],
        [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"]
        ],
        [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
        ],
        [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
        ],
    ]
    for test in tests:
        print('[')
        solution.solve(test)
        for i in test:
            print('\t', i, end=',\n')
        print(']')
        print()


if __name__ == "__main__":
    main()
