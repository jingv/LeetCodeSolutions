#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   InterView29-spiralOrder.py
@Time    :   2020/06/05 16:54:51
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def spiralOrder(self, matrix):
        # 执行用时 :48 ms, 在所有 Python3 提交中击败了75.27%的用户
        # 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
        if not matrix or not matrix[0]:
            return []
        left, right, top, bottom, result = 0, len(
            matrix[0]), len(matrix), 0, []
        while left < right and bottom < top:
            # 下横向
            for i in range(left, right):
                result.append(matrix[bottom][i])
            bottom += 1
            # 右竖向
            for i in range(bottom, top):
                result.append(matrix[i][right - 1])
            right -= 1
            # 上横向
            for i in range(right - 1, left - 1, -1):
                if top != bottom:
                    result.append(matrix[top - 1][i])
            top -= 1
            # 左竖向
            for i in range(top - 1, bottom - 1, -1):
                if left != right:
                    result.append(matrix[i][left])
            left += 1
        return result


def main():
    tests = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1]],
        [[]],
        [[1], [2], [3]],
        [[1, 2, 3]],
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ]
    solution = Solution()
    for test in tests:
        print(solution.spiralOrder(test))


if __name__ == "__main__":
    main()
