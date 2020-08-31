#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview64-sumNums.py
@Time    :   2020/06/02 15:36:20
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def helper(self, A, B):
        ans = B and self.helper(A << 1, B >> 1)
        ans += B & 1 and A
        return ans

    def sumNums(self, n):
        return self.helper(n, n + 1) >> 1


def main():
    tests = [3, 9]
    solution = Solution()
    for test in tests:
        print(solution.sumNums(test))


if __name__ == "__main__":
    main()
