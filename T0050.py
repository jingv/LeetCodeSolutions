#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0050.py
@Time    :   2020/05/11 08:41:46
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def myPow(self, x, n):
        multi = True if n > 0 else False
        n = abs(n)
        result = 1
        for _ in range(n):
            result = result * x
        return result if multi else 1/result


def main():
    tests = [(2, 10), (2.1, 3), (2, -2)]
    solution = Solution()
    for x, n in tests:
        print(solution.myPow(x, n))


if __name__ == "__main__":
    main()
