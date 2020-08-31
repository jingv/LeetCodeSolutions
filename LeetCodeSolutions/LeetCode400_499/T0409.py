#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0409.py
@Time    :   2020/03/19 09:09:28
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def longestPalindrome(self, s: str) -> int:
    def longestPalindrome(self, s):
        # 只要字符串中的字符A(举例)的个数为2的倍数，那么就可以将所有的A插入回文串
        # 如果字符串中的字符A的个数不是2的倍数：
        #   A只有一个：那么A只能作为中间那个字符插入回文串，且回文串不能添加别的单个字符
        #   A>2个但是为奇数个：可以将2的倍数个插入回文串，之后相当于只有一个的情况
        # 执行用时 :64 ms, 在所有 Python3 提交中击败了6.94%的用户
        # 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.32%的用户
        result, add1 = 0, False
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        for item in hash_map:
            result += (hash_map[item] // 2) * 2
            if not add1:
                if hash_map[item] % 2:
                    add1 = True
        return result+1 if add1 else result

    def longestPalindrome2(self, s):
        # 算法优化
        # 去重后的s
        # 执行用时 :36 ms, 在所有 Python3 提交中击败了70.67%的用户
        # 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.32%的用户
        single_s = list(set(s))
        result = 0
        for char in single_s:
            result += s.count(char) // 2 * 2
        return result if len(s) == result else result + 1


def main():
    tests = ['abccccdd', ]
    solution = Solution()
    for test in tests:
        print(solution.longestPalindrome2(test))


if __name__ == "__main__":
    main()
