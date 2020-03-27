#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0914.py
@Time    :   2020/03/27 10:51:06
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def hasGroupsSizeX(self, deck: List[int]) -> bool:
    def hasGroupsSizeX(self, deck):
        # 执行用时 :88 ms, 在所有 Python3 提交中击败了72.80%的用户
        # 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.38%的用户
        if not deck:
            return False
        nums = []
        for i in list(set(deck)):
            nums.append(deck.count(i))
        import math
        result = nums[0]
        for num in nums[1:]:
            result = math.gcd(result, num)
        return False if result == 1 else True


def main():
    solution = Solution()
    tests = [
        [1, 2, 3, 4, 4, 3, 2, 1],
        [1,  1, 1, 2, 2, 2, 3, 3],
        [1],
        [1, 1],
        [1, 1, 2, 2, 2, 2],
        [],
    ]
    for test in tests:
        print(solution.hasGroupsSizeX(test))


if __name__ == "__main__":
    main()
