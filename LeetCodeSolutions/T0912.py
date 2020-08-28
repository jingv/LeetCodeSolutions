#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0912.py
@Time    :   2020/03/31 15:28:56
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


def quick_sort(nums, left, right):
    # 快速排序
    if left >= right:
        return nums
    midnum = nums[left]
    i = left
    j = right
    while i < j:
        while nums[j] > midnum and i < j:
            j -= 1
        nums[i] = nums[j]
        while nums[i] < midnum and i < j:
            i += 1
        nums[j] = nums[i]
    nums[j] = midnum
    quick_sort(nums, left, j)
    quick_sort(nums, i + 1, right)
    return nums


def merge_sort(nums):
    pass


def main():
    tests = [
        [1, 2, 3, 4, 5, 9, 8, 7, 6],
        [],
        [1]
    ]
    for test in tests:
        print(quick_sort(test, 0, len(test)-1))
        print(merge_sort(test))


if __name__ == "__main__":
    main()
