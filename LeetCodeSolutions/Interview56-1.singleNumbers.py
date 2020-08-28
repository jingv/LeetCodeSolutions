#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview56-1.singleNumbers.py
@Time    :   2020/04/28 13:34:32
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def singleNumbers(self, nums):
        # 执行用时 :56 ms, 在所有 Python3 提交中击败了79.65%的用户
        # 内存消耗 :14.7 MB, 在所有 Python3 提交中击败了100.00%的用户
        temp = 0 
        for i in nums:
            temp = temp ^ i
        div = 1
        while div & temp == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


def main():
    tests = [[4, 1, 4, 6], [1, 2, 10, 4, 1, 4, 3, 3]]
    solution = Solution()
    for test in tests:
        print(solution.singleNumbers(test))


if __name__ == "__main__":
    main()
