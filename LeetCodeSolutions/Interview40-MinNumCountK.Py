#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview40-MinNumCountK.Py
@Time    :   2020/03/20 08:53:31
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    def getLeastNumbers(self, arr, k):
        # 排序返回
        # 执行用时 :76 ms, 在所有 Python3 提交中击败了74.73%的用户
        # 内存消耗 :14.1 MB, 在所有 Python3 提交中击败了100.00%的用户
        return sorted(arr)[:k]

    def getLeastNumbers2(self, arr, k):
        import heapq
        # 使用堆模块 heapq
        # 执行用时 :124 ms, 在所有 Python3 提交中击败了57.67%的用户
        # 内存消耗 :15.4 MB, 在所有 Python3 提交中击败了100.00%的用户
        return heapq.nsmallest(k, arr)


def main():
    tests = [([3, 2, 1], 2), ([0, 1, 2, 1], 1), ([], 1)]
    solution = Solution()
    for arr, k in tests:
        print(solution.getLeastNumbers(arr, k), " ",
              solution.getLeastNumbers2(arr, k))


if __name__ == "__main__":
    main()
