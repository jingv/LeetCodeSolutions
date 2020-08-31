#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0696.py
@Time    :   2020/08/10 19:35:29
@Author  :   JingV
@Version :   1.0
@Contact :   dllOoOllb.com
@Desc    :   None
'''


class Solution():
    def countBinarySubstrings(self, s):
        seq = [0, 1]
        result = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                seq[-1] += 1
            else:
                result.append(min(seq))
                seq[0], seq[1] = seq[1], 1
        result.append(min(seq))
        return sum(result)


def main():
    solution = Solution()
    tests = [
        # "00110011",
        "10101",
    ]
    for test in tests:
        print(solution.countBinarySubstrings(test))


if __name__ == "__main__":
    main()
