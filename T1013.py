#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T1013.py
@Time    :   2020/03/11 14:32:32
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def canThreePartsEqualSum(self, A: List[int]) -> bool:
    def canThreePartsEqualSum(self, A):
        avg, remainder = divmod(sum(A), 3)
        if remainder != 0 or len(A) < 3:
            return False
        left, right = 0, len(A)-1
        item1_sum, item2_sum = A[left], A[right]
        # 将A分为3段，[:left+1] [left+1: right] [right-1:]
        # 保证A[left+1:right]中存在数值        
        while left < right-1:
            if item1_sum != avg:
                left += 1
                item1_sum += A[left]
                continue
            if item2_sum != avg:
                right -= 1
                item2_sum += A[right]
                continue
            return True
        return False


def main():
    tests = [
        [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1],
        [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1],
        [3, 3, 6, 5, -2, 2, 5, 1, -9, 4],
        [1, 1, 1],
        [6, 1, 1, 13, -1, 0, -10, 20],
        [18, 12, -18, 18, -19, -1, 10, 10],
        [1, -1, 1, -1],
    ]
    solution = Solution()
    for test in tests:
        print(solution.canThreePartsEqualSum(test))


if __name__ == "__main__":
    main()
