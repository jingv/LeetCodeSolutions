#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0003.py
@Time    :   2020/05/03 01:12:05
@Author  :   JingV
@Version :   1.0
@Contact :   dllOoOllb.com
@Desc    :   None
'''


class Solution():
    def lenthOfLongstSubString(self, s):
        if len(s) <= 1:
            return len(s)
        result, start = 0, 0
        for i in range(start + 1, len(s)):
            while(s[i] in s[start: i]):
                start += 1
            if i - start + 1 > result:
                result = i - start + 1
        return result


def main():
    tests = ["abcabcbb", "pwwkew", "bbbbbbb", "1", "aa"]
    # tests = ["aa"]
    solution = Solution()
    for test in tests:
        print(solution.lenthOfLongstSubString(test))


if __name__ == "__main__":
    main()
