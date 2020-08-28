#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview10-01sorted-merge.py
@Time    :   2020/07/07 14:40:23
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify A in-place instead.
        """
        index_a, index_b = 0, 0
        while index_a < m and index_b < n:
            if A[index_a] > B[index_b]:
                A[index_a + 1:] = A[index_a: m]
                A[index_a] = B[index_b]
                index_a, index_b, m = index_a + 1, index_b + 1, m + 1
            else:
                index_a += 1
        if index_b < n:
            A[index_a:] = B[index_b:]


def main():
    solution = Solution()
    tests = [
        # [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[2, 0], 1, [1], 1],
    ]
    for A, m, B, n in tests:
        solution.merge(A, m, B, n)
        print(A)


if __name__ == "__main__":
    main()
