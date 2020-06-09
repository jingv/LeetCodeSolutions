#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview46-translateNum.py
@Time    :   2020/06/09 09:18:16
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def translateNum(self, num):
        # 执行用时 :36 ms, 在所有 Python3 提交中击败了83.43%的用户
        # 内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
        num_str = str(num)
        first, second = 1, 0
        if len(num_str) >= 2:
            if 10 <= int(num_str[:2]) <= 25:
                second = 2
            else:
                second = 1
        else:
            return first
        for k in range(3, len(num_str) + 1):
            if 10 <= int(num_str[k-2: k]) <= 25:
                first, second = second, first + second
            else:
                first, second = second, second
        return second


def main():
    tests = [12258, 102]
    solution = Solution()
    for test in tests:
        print(solution.translateNum(test))


if __name__ == "__main__":
    main()
