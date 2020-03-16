#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview01-06CompressString.py
@Time    :   2020/03/16 08:39:54
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def compressString(self, S):
        # 暴力循环
        # 执行用时 :80 ms, 在所有 Python3 提交中击败了37.40%的用户
        # 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
        if not S:
            return S
        count, current, result = 0, S[0], ''
        for i in S:
            if i == current:
                count += 1
            else:
                result, current, count = result+current+str(count), i, 1
        result += (current + str(count))
        return result if len(result) < len(S) else S

    def compressString2(self, S):
        # 双指针法
        # 执行用时 :92 ms, 在所有 Python3 提交中击败了23.92%的用户
        # 内存消耗 :13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
        if not S:
            return S
        i, j, result = 0, 1, ''
        while j < len(S):
            if S[i] == S[j]:
                j += 1
            else:
                result, i, j = result+S[i]+str(j-i), j, j+1
        result += (S[i] + str(j-i))
        return result if len(result) < len(S) else S


def main():
    tests = ["aabcccccaaa", "abbccd", ""]
    solution = Solution()
    for test in tests:
        print(solution.compressString2(test))


if __name__ == "__main__":
    main()
