#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0005.py
@Time    :   2020/05/21 08:39:13
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def longestPalindrome(self, s):
        if not s:
            return ""
        reverse_s = s[::-1]
        left, right = 0, len(s)-1
        while left < len(s)-1 and reverse_s[left] != s[left]:
            left += 1
        while right > left and reverse_s[right] != s[right]:
            right -= 1
        return s[left: right + 1]


def main():
    tests = ["babad", "cbbd", "a", "", "ac"]
    solution = Solution()
    for test in tests:
        print(solution.longestPalindrome(test))


if __name__ == "__main__":
    main()
