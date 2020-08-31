#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0063.py
@Time    :   2020/07/06 08:49:38
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def uniquePathsWithObstacles(self, obstacleGrid):
        """Very Good, TimeOut"""
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0

        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0] == 0:
            return 1

        return self.uniquePathsWithObstacles(obstacleGrid[1:]) + self.uniquePathsWithObstacles([i[1:] for i in obstacleGrid])

    def uniquePathsWithObstaclesDP(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        colum, raw = len(obstacleGrid[0]), len(obstacleGrid)
        for i in range(raw):
            for j in range(colum):
                if obstacleGrid[i][j] == 0:
                    if i == j == 0:
                        # 起始位置，初始化为1
                        obstacleGrid[i][j] = 1
                    else:
                        left = obstacleGrid[i][j - 1] if j > 0 else 0
                        up = obstacleGrid[i - 1][j] if i > 0 else 0
                        obstacleGrid[i][j] = left + up
                else:
                    # 可以到达障碍物的路径为0（障碍物不可到达）
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]


def main():
    solution = Solution()
    tests = [
        [
            [0]
        ],
        [
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0]
        ],
        [
            [0],
            [0],
            [0],
            [0],
        ],
        [
            [0],
            [0],
            [1],
            [0],
        ],
        [
            [0, 0],
            [0, 0]
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ]
    for test in tests:
        print(solution.uniquePathsWithObstacles(test), " <==>", solution.uniquePathsWithObstaclesDP(test))


if __name__ == "__main__":
    main()
