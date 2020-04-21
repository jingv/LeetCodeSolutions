#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T1248.py
@Time    :   2020/04/21 08:44:30
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def numberOfSubarrays(self, nums, k):
        # 执行用时 :988 ms, 在所有 Python3 提交中击败了73.55%的用户
        # 内存消耗 :20.1 MB, 在所有 Python3 提交中击败了25.00%的用户
        n, odd, result = len(nums), [-1], 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        for i in range(1, len(odd) - k):
            result += (odd[i] - odd[i-1]) * (odd[i + k] - odd[i + k - 1])
        return result


def main():
    tests = [
        [[1, 1, 2, 1, 1], 3],
        [[2, 4, 6], 1],
        [[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2]
    ]
    solution = Solution()
    for nums, k in tests:
        print(solution.numberOfSubarrays(nums, k))


if __name__ == "__main__":
    main()
