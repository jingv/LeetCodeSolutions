#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0378.py
@Time    :   2020/07/02 16:53:47
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) == 0:
            return
        if len(matrix) == 1:
            # if len(matrix[0]) < k:
            #     return
            return matrix[0][k - 1]
        first, second = matrix.pop(), matrix.pop()
        first_index, second_index = 0, 0
        sorted_result = []
        while first_index < len(first) and second_index < len(second):
            if first[first_index] < second[second_index]:
                sorted_result.append(first[first_index])
                first_index += 1
            else:
                sorted_result.append(second[second_index])
                second_index += 1
        sorted_result += first[first_index:] if first[first_index:] else second[second_index:]
        matrix.append(sorted_result)
        return self.kthSmallest(matrix, k)


def main():
    tests = [
        [
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]
            ],
            8
        ],
    ]
    solution = Solution()
    for matrix, k in tests:
        print(solution.kthSmallest(matrix, k))


if __name__ == "__main__":
    main()
