#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0016.py
@Time    :   2020/06/24 10:06:24
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None
        nums.sort()
        result = sum(nums[0: 3])
        for i in range(0, len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                item_sum = nums[i] + nums[left] + nums[right]
                if item_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif item_sum > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    return item_sum
                if abs(result - target) > abs(item_sum - target):
                    result = item_sum
        return result


def main():
    tests = [
        ([-1, 2, 1, -4], 1),
        ([-1, 2, -400], 1),
    ]
    solution = Solution()
    for nums, target in tests:
        print(solution.threeSumClosest(nums, target))


if __name__ == "__main__":
    main()
