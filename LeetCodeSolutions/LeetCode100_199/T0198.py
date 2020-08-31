#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0198.py
@Time    :   2020/05/29 15:53:00
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def rob(self, nums):
        # 递归 => 喜闻乐见的超时
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-1]))

    def rob2(self, nums):
        # 循环 - 通过存储前n项的结果
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        di = [0 for i in range(len(nums))]
        di[0] = nums[0]
        di[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            di[i] = max(di[i - 2] + nums[i], di[i-1])
        return di[-1]

    def rob3(self, nums):
        # 动态规划 => 芜湖，有点斐波拉契的意思哦
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)
        return second


def main():
    tests = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2],
        [],
        [1],
    ]
    solution = Solution()
    for test in tests:
        print(solution.rob3(test))


if __name__ == "__main__":
    main()
