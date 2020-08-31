#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0009.py
@Time    :   2020/06/10 08:36:11
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def isPalindrome(self, x):
        try:
            _ = x - 1
        except TypeError:
            return False
        x_str = str(x)
        left, right = 0, len(x_str) - 1
        while left < right:
            if x_str[left] != x_str[right]:
                break
            left, right = left + 1, right - 1
        else:
            return True
        return False


def main():
    tests = [10, -121, 121, 1, 1221, 1231, 0, 999999, "this is a string"]
    solution = Solution()
    for test in tests:
        print(solution.isPalindrome(test))


if __name__ == "__main__":
    main()
            
