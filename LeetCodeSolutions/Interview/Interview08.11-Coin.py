#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview08.11-Coin.py
@Time    :   2020/04/23 09:23:49
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def waysToChange(self, n):
        # 数学方法， 学不来学不来
        # 执行用时 :64 ms, 在所有 Python3 提交中击败了98.01%的用户
        # 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
        '''
        n:      int
        return: int
        '''
        result = 0
        for i in range(n // 25 + 1):
            rest = n - i * 25
            a, b = rest // 10, rest % 10 // 5
            result += (a + 1) * (a + b + 1)
        return result % (10 ** 9 + 7)


def main():
    tests = [5, 10, 100, 1000, 10000]
    solution = Solution()
    for test in tests:
        print(solution.waysToChange(test))


if __name__ == "__main__":
    main()
