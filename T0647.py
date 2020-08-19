#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0647.py
@Time    :   2020/08/19 10:29:07
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def countSubstring(self, s):
        ''' 暴力!!! '''
        def is_palindrome(s):
            exter_x = '#'
            for i in s:
                exter_x += (i + '#')
            left, right = 0, len(exter_x) - 1
            while left < right:
                if exter_x[left] != exter_x[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        len_s, result = len(s), 0
        for i in range(len_s):
            for j in range(i, len_s):
                if is_palindrome(s[i: j + 1]):
                    result += 1
        return result

    def countSubstring2(self, s):
        def check(s, l, r):
            num = 0
            # 以中心字符为基准向两边扩散
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                num += 1
            return num
        num = 0
        for i in range(len(s)):
            # 以当前字符为奇数长度的字符串的中心字符
            num += check(s, i, i)
            if i == len(s)-1:
                continue
            # 以当前字符与下一个字符作为偶数长度字符串的中心字符
            num += check(s, i, i+1)
        return num


def main():
    solution = Solution()
    tests = [
        '',
        'abc',
        'aaa',
    ]
    for test in tests:
        # print(solution.countSubstring(test))
        print(solution.countSubstring2(test))


if __name__ == "__main__":
    main()
