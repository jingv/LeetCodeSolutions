#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0392.py
@Time    :   2020/07/27 09:18:00
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def isSubsequence(self, s, t):
        len_s, len_t = len(s), len(t)
        cur_s, cur_t = 0, 0
        while cur_t < len_t and cur_s < len_s:
            if s[cur_s] == t[cur_t]:
                cur_s += 1
            cur_t += 1
        return cur_s == len_s


def main():
    solution = Solution()
    tests = [
        ['abc', 'ahbhdc'],
        ['axc', 'ahbhdc'],
        ['', 'ahbhdc'],
    ]
    for s, t in tests:
        print(solution.isSubsequence(s, t))


if __name__ == "__main__":
    main()
