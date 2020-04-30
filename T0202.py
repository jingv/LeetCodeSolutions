#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0202.py
@Time    :   2020/04/30 15:58:16
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def isHappy(self, n):
        def forSum(num):
            result = 0
            while num:
                result += (num % 10) ** 2
                num //= 10
            return result

        nums = []
        while True:
            if n in nums or n == 1:
                break
            else:
                nums.append(n)
            n = forSum(n)

        return n == 1


def main():
    tests = [10, 19, 116]
    solution = Solution()
    for test in tests:
        print(solution.isHappy(test))


if __name__ == "__main__":
    main()
