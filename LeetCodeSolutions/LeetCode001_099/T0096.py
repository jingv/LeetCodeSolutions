#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0096.py
@Time    :   2020/07/15 08:48:54
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def numTrees(self, n):
        result = [0 for _ in range(n + 1)]
        result[0], result[1] = 1, 1
        # i 为根节点的值
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                result[i] += result[j - 1] * result[i - j]
        return result[-1]


def main():
    solution = Solution()
    tests = [3]
    for test in tests:
        print(solution.numTrees(test))


if __name__ == "__main__":
    main()
