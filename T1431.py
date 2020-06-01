#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T1431.py
@Time    :   2020/06/01 08:53:00
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def kidsWithCandies(self, candies, extraCandies):
        max_candi = max(candies)
        result = []
        for i in candies:
            result.append(i + extraCandies >= max_candi)
        return result


def main():
    tests = [
        [[2, 3, 5, 1, 3], 3],
        [[4, 2, 1, 1, 2], 1]
    ]
    solution = Solution()
    for candies, extraCandies in tests:
        print(solution.kidsWithCandies(candies, extraCandies))


if __name__ == "__main__":
    main()
