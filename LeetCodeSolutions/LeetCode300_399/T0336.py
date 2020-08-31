#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0336.py
@Time    :   2020/08/06 09:26:13
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def palindromePairs(self, words):
        def isPalindrome(s1, s2=''):
            len_s1, len_s2 = len(s1), len(s2)
            if len_s1 == 0 or len_s2 == 0:
                temp = s1 if len_s1 != 0 else s2
                if len(temp) <= 1:
                    return True
                else:
                    temp_ex = '#'
                    for i in temp:
                        temp_ex += (i + '#')
                    left, right = 0, len(temp_ex)-1
                    while left < right:
                        if temp_ex[left] != temp_ex[right]:
                            return False
                        left, right = left + 1, right - 1
                    return True

            if len_s1 == len_s2:
                return s1 == s2[::-1]
            elif len_s1 > len_s2:
                return s1[:len_s2][::-1] == s2 and isPalindrome(s1[len_s2:])
            else:
                return s1 == s2[-len_s1:][::-1] and isPalindrome(s2[:-len_s1])

        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if isPalindrome(words[i], words[j]):
                    result.append([i, j])
        return result


def main():
    solution = Solution()
    tests = [
        ["abcd", "dcba", "lls", "s", "sssll"],
        ["bat", "tab", "cat"],
    ]
    for test in tests:
        print(solution.palindromePairs(test))


if __name__ == "__main__":
    main()
