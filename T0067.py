#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0067.py
@Time    :   2020/06/23 14:24:26
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def addBinary(self, a, b):
        result, flag = "", "0"
        for i in range(-1, -max(len(a), len(b)) - 2, -1):
            try:
                x = a[i]
            except Exception:
                x = "0"
            try:
                y = b[i]
            except IndexError:
                y = "0"
            if x == y == "1":
                result = flag + result
                flag = "1"
            # x 与 y 不同时为 "1"
            elif x != y:
                if flag == "1":
                    result = "0" + result
                else:
                    result = "1" + result
            # x 与 y 同时为 "0"
            else:
                result = flag + result
                if flag == "1":
                    flag = "0"
        return result if len(result) == 1 or result[0] == "1" else result[1:]


def main():
    tests = [
        ("1", "11"),
        ("1010", "1011"),
        ("111", "0"),
        ("0", "0"),
        ("", "")
    ]
    solution = Solution()
    for a, b in tests:
        print(solution.addBinary(a, b))


if __name__ == "__main__":
    main()
