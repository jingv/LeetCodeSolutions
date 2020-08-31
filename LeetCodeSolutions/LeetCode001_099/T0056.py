#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0056.py
@Time    :   2020/04/16 09:02:41
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def merge(self, intervals):
        # 先排序，后处理；注意为空的情况
        # 执行用时 :56 ms, 在所有 Python3 提交中击败了66.07%的用户
        # 内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        intervals.sort()
        if not intervals:
            return []
        left, right, result = intervals[0][0], intervals[0][1], []
        for item in intervals[1:]:
            if not(item[1] < left or right < item[0]):
                left, right = min(left, item[0]), max(right, item[1])
            else:
                result.append([left, right])
                left, right = item[0], item[1]
        else:
            result.append([left, right])
        return result


def main():
    tests = [
        [],
        [[1, 2]],
        [[1, 4], [4, 5]],
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[2, 3], [4, 5], [6, 7], [1, 10]],
    ]
    solution = Solution()
    for test in tests:
        print(solution.merge(test))


if __name__ == "__main__":
    main()
