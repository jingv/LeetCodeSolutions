#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0169.py
@Time    :   2020/03/13 10:07:19
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def majorityElement(self, nums):
        # 现将数据排序，则处于中间位置的就是多数元素
        # 执行用时 :36 ms, 在所有 Python3 提交中击败了99.03%的用户
        # 内存消耗 :14.9 MB, 在所有 Python3 提交中击败了5.04%的用户
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement2(self, nums):
        # 使用hashmap，遍历列表，返回数量大于总数量1/2的数
        # 执行用时 :84 ms, 在所有 Python3 提交中击败了78.93%的用户
        # 内存消耗 :15.2 MB, 在所有 Python3 提交中击败了5.04%的用户
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            if hashmap[num] > len(nums) / 2:
                return num

    def majorityElement3(self, nums):
        # Boyer-Moore 投票算法（摩尔投票法）
        # 从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个
        # 执行用时 :56 ms, 在所有 Python3 提交中击败了87.78%的用户
        # 内存消耗 :14.9 MB, 在所有 Python3 提交中击败了5.04%的用户
        result, count = 0, 0
        for num in nums:
            if count == 0:
                result = num
                count = 1
                continue
            if num == result:
                count += 1
            else:
                count -= 1
        return result


def main():
    solution = Solution()
    tests = [[3, 2, 3], [2, 2, 1, 1, 1, 2, 2], [1]]
    for test in tests:
        print(solution.majorityElement3(test))


if __name__ == "__main__":
    main()
