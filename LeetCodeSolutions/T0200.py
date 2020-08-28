#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0200.py
@Time    :   2020/04/20 08:40:23
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def numIslands(self, grid):
        # 方法DFS(Depth-First-Search)
        # 执行用时 :168 ms, 在所有 Python3 提交中击败了20.85%的用户
        # 内存消耗 :14.1 MB, 在所有 Python3 提交中击败了6.67%的用户
        result, temp = 0, []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    grid[i][j] = "0"
                    temp.append([i, j])
                while temp:
                    x, y = temp.pop(0)
                    for position in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                        if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]) and grid[position[0]][position[1]] == "1":
                            grid[position[0]][position[1]] = 0
                            temp.append(position)
        return result


def main():
    tests = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ]
    ]
    solution = Solution()
    for test in tests:
        print(solution.numIslands(test))


if __name__ == "__main__":
    main()
