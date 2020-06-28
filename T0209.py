#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0209.py
@Time    :   2020/06/28 14:40:51
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def minSubArrayLen(self, s, nums):
        # 弹性数组/双指针
        if sum(nums) < s:
            return 0
        result = len(nums) if nums[0] < s else 1
        if result == 1:
            return result
        left, right = 0, 1
        while right < len(nums):
            # left = right + 1
            if left > right:
                right += 1
            else:
                if sum(nums[left: right + 1]) >= s:
                    if result > (right - left + 1):
                        result = right - left + 1
                        if result == 1:
                            return result
                    left += 1
                else:
                    right += 1
        return result


def main():
    tests = [
        [7, [2, 3, 1, 2, 4, 3]],
        [7, [8]],
        [7, [0, 2, 4, 8]],
        [7, []],
        [7, [0, 1, 2]],
        [7, [1, 8, 2]],
        [6, [10, 2, 3]],
    ]
    solution = Solution()
    for s, nums in tests:
        print(solution.minSubArrayLen(s, nums))


if __name__ == "__main__":
    main()
