#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0045.py
@Time    :   2020/05/04 08:50:06
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def jump(self, nums):
        # maxpos    能达到的最远的item的下标
        # end       记[i: end]之间的元素能到达的最远位置(maxpos)， 类似于循环结束的条件
        # step      跳跃的次数

        # 执行用时 :56 ms, 在所有 Python3 提交中击败了80.36%的用户
        # 内存消耗 :15.1 MB, 在所有 Python3 提交中击败了12.50%的用户
        maxpos, end, step = 0, 0, 0
        for i in range(len(nums) - 1):
            if maxpos >= i:
                maxpos = max(maxpos, i + nums[i])
                if i == end:
                    end = maxpos
                    step += 1
        return step


def main():
    tests = [
        [2, 3, 1, 1, 4],
    ]
    solution = Solution()
    for test in tests:
        print(solution.jump(test))


if __name__ == "__main__":
    main()