#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0038.py
@Time    :   2020/05/12 15:21:23
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def countAndSay(self, n):
        if n < 1:
            return ""
        loop = 1
        result = "1"
        while loop < n:
            temp = ""
            count, cur_string = 1, result[0]
            for i in range(1, len(result)):
                if cur_string != result[i]:
                    temp = temp + str(count) + cur_string
                    count, cur_string = 1, result[i]
                else:
                    count += 1
            result = temp + str(count) + cur_string
            loop += 1
        return result
                

def main():
    tests = [1, 2, 3, 4, 5]
    solution = Solution()
    for test in tests:
        print(solution.countAndSay(test))


if __name__ == "__main__":
    main()
