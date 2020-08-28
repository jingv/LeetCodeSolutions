#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0017.py
@Time    :   2020/08/26 08:55:40
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        # bfs
        key_ref = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []
        queue = [(digits, '')]
        while queue:
            source_str, cur_res = queue.pop(0)

            if len(source_str) == 0:
                result.append(cur_res)
                continue

            chars = key_ref[source_str[0]]
            for char in chars:
                new_res = cur_res + char
                queue.append((source_str[1:], new_res))
        return result

    def letterCombinations_dfs(self, digits):
        if len(digits) == 0:
            return []
        # bfs
        key_ref = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []

        def help(source_str, cur_res):
            if not source_str:
                result.append(cur_res)
                return
            for i in key_ref[source_str[0]]:
                help(source_str[1:], cur_res + i)

        help(digits, '')
        return result


def main():
    solution = Solution()
    tests = ['234', ]
    for test in tests:
        print(solution.letterCombinations(test))
        print(solution.letterCombinations_dfs(test))


if __name__ == "__main__":
    main()
