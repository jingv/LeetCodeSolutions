#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0015.py
@Time    :   2020/06/12 11:14:16
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                # 当前为剩下数字中的最小值，最小值大于0，没必要继续循环
                break
            if i > 0 and nums[i] == nums[i - 1]:
                # 当前数字与上一个数字相同
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = [nums[i], nums[left], nums[right]]
                if sum(temp) == 0:
                    result.append(temp)
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum(temp) < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


def main():
    tests = [
        [-1, 0, 1, 2, -1, -4],
    ]
    solution = Solution()
    for test in tests:
        print(solution.threeSum(test))


if __name__ == "__main__":
    main()
