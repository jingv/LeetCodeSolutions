#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview43-01 CountDigitOne.py
@Time    :   2020/05/12 16:14:49
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def countDigitOne(self, n):
        temp = []
        while n > 0:
            temp.append(n % 10 + 1)
            n = n // 10
        result = 0
        for i in range(len(temp)):
            sub_count = 1
            for j in range(len(temp)):
                if i == j:
                    continue
                sub_count *= temp[j]
            result += sub_count
        return result


def main():
    tests = [100, 10, 12, 13, 199]
    solution = Solution()
    for test in tests:
        print(solution.countDigitOne(test))


if __name__ == "__main__":
    main()
