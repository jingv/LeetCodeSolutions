#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0529.py
@Time    :   2020/08/20 15:49:37
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def updateBoard(self, board, click):
        cur_item = board[click[0]][click[1]]
        if cur_item == "M":
            board[click[0]][click[1]] = 'X'
            return board
        elif cur_item == "E":
            row, column = len(board), len(board[0])
            import numpy as np
            # 创建numpy数组对象对象
            board_exp = np.array([[0 for _ in range(column + 2)]
                                  for _ in range(row + 2)])
            # 转换board, 雷为1, 其余为0
            board_trans = []
            for i in range(row):
                temp = []
                for j in range(column):
                    if board[i][j] == 'M':
                        temp.append(1)
                    else:
                        temp.append(0)
                board_trans.append(temp)
            # 用转换后的board替换numpy数组对象的相应位置
            board_exp[1:1+row, 1:1+column] = np.array(board_trans)
            # 设置卷积内核
            kernel = np.array([[1 for _ in range(3)] for _ in range(3)])

            # 将要检查的点入队
            queue = [click]
            # 区域的八个方向
            direction = [[0, 1], [0, -1], [1, 1], [1, 0],
                         [1, -1], [-1, -1], [-1, 0], [-1, 1]]
            # 开始更新board
            while queue:
                temp = queue.pop(0)
                # 如果当前位置的值不为E或不为M, 则说明这个位置已经被处理过了, 不需要在处理
                if board[temp[0]][temp[1]] != 'E' and board[temp[0]][temp[1]] != 'M':
                    continue
                # print("temp[0] = {}, temp[1] = {}".format(temp[0], temp[1]))
                # 求卷积和 - 范围内雷的个数
                mine_count = np.sum(kernel*board_exp[temp[0]: temp[0]+3, temp[1]: temp[1] + 3])
                # 当前区域内有雷, 打印数字, 并不向下扩展
                if mine_count > 0:
                    board[temp[0]][temp[1]] = str(mine_count)
                # 当前区域内无雷, 检查相邻区域内是否有雷
                else:
                    # 添加无雷标志
                    board[temp[0]][temp[1]] = 'B'
                    # 将检查点附近的区域入队
                    for direc in direction:
                        new_r, new_c = temp[0] + direc[0], temp[1] + direc[1]
                        if new_r in range(row) and new_c in range(column):
                            queue.append((new_r, new_c))
        return board


def main():
    solution = Solution()
    tests = [
        [
            [
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'M', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
            ],
            (3, 0)
        ],
        [
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ],
            (1, 2),
        ],
    ]
    for board, click in tests:
        # print(solution.updateBoard(board, click))
        for i in solution.updateBoard(board, click):
            print(i)
        print()


if __name__ == "__main__":
    main()
