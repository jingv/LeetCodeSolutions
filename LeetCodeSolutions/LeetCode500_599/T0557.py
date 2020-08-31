#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   JingV
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def reverseWords(self, s):
        '''循环迭代'''
        temp, result = '', ''
        for char in s:
            if char == ' ':
                result += (temp[::-1] + ' ')
                temp = ''
            else:
                temp += char
        return result + temp[::-1]

    def reverseWords2(self, s):
        '''内置函数'''
        return ' '.join((s[::-1].split(' '))[::-1])


def main():
    solution = Solution()
    tests = [
        "Let's take LeetCode contest",
    ]
    for test in tests:
        print(solution.reverseWords2(test))


if __name__ == '__main__':
    main()
