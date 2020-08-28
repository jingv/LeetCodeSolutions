#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T1071.py
@Time    :   2020/03/12 08:35:00
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


import math


class Solution():
    def gcdOfStrings(self, str1, str2):
        # 执行用时 :132 ms, 在所有 Python3 提交中击败了5.99%的用户
        # 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了7.48%的用户
        result = ''
        max_result = ''
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                break
            result += str1[i]
            if str1.replace(result, "") == str2.replace(result, "") == "":
                max_result = result
        return max_result

    def gcdOfStrings2(self, str1, str2):
        # 数学方法：找到两个字符串的最大公约数，然后判断最大公约数长度的子字符串是否是字符串的最长公因子
        # 执行用时 :40 ms, 在所有 Python3 提交中击败了44.31%的用户
        # 内存消耗 :13.4 MB, 在所有 Python3 提交中击败了7.48%
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if str1.replace(candidate, "") == str2.replace(candidate, "") == "":
            return candidate
        return ""


def main():
    tests = [("ABCABC", "ABC"), ("ABABAB", "ABAB"), ("LEFT", "CODE")]
    solution = Solution()
    for str1, str2 in tests:
        print(solution.gcdOfStrings(str1, str2))
        print(solution.gcdOfStrings2(str1, str2))


if __name__ == "__main__":
    main()
