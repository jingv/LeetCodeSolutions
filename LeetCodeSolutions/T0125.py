#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0125.py
@Time    :   2020/06/19 11:23:16
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def isPalindrome(self, s):
        s_handled = ""
        for i in s:
            if i.isalnum():
                s_handled = s_handled + i.lower() + "#"
        s_handled = s_handled[:-1]
        left, right = 0, len(s_handled) - 1
        while left <= right:
            if s_handled[left] != s_handled[right]:
                return False
            left, right = left + 1, right - 1
        return True


def main():
    tests = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "0p",
        "",
        '1',  
    ]
    solution = Solution()
    for test in tests:
        print(solution.isPalindrome(test))


if __name__ == "__main__":
    main()
