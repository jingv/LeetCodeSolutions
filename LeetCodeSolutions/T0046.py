#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0046.py
@Time    :   2020/04/22 13:33:24
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def permute(self, nums):
        '''
        回溯法
        nums:   List[int]
        return: List[List[int]]
        '''
        result = []

        def backtrack(nums, temp):
            if len(nums) == 1:
                result.append(temp + nums)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], temp + [nums[i]])

        backtrack(nums, [])
        return result


def main():
    tests = [[1, 2, 3]]
    solution = Solution()
    for test in tests:
        print(solution.permute(test))


if __name__ == "__main__":
    main()
