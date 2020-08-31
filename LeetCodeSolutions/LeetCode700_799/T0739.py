#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0739.py
@Time    :   2020/06/11 21:44:09
@Author  :   JingV
@Version :   1.0
@Contact :   dllOoOllb.com
@Desc    :   None
'''


class Solution():
    def dailyTemperatuers(self, T):
        # 单调栈
        stack, result = [], [0 for i in range(0, len(T))]
        for i in range(0, len(T)):
            while stack and T[i] > T[stack[-1]]:
                pre_index = stack.pop()
                result[pre_index] = i - pre_index
            stack.append(i)
        return result


def main():
    tests = [
        [73, 74, 75, 71, 69, 72, 76, 73],
    ]
    solution = Solution()
    for test in tests:
        print(solution.dailyTemperatuers(test))


if __name__ == "__main__":
    main()
