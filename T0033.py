#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0033.py
@Time    :   2020/04/27 11:14:42
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def search(self, nums: List[int], target: int) -> int
    def search(self, nums, target):
        # 二分法查找
        # 执行用时 :44 ms, 在所有 Python3 提交中击败了56.57%的用户
        # 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了7.69%的用户
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 左边是有序的
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


def main():
    tests = [
        [
            [4, 5, 6, 7, 0, 1, 2],
            0
        ],
        [
            [4, 5, 6, 7, 0, 1, 2],
            3,
        ],
    ]
    solution = Solution()
    for nums, target in tests:
        print(solution.search(nums, target))


if __name__ == "__main__":
    main()
