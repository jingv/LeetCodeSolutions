#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0415addStrings.py
@Time    :   2020/08/03 08:57:52
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def addStrings(self, num1, num2):
        max_len = max(len(num1), len(num2))
        format_str = "{:0>" + str(max_len) + "}"
        num1 = format_str.format(num1)
        num2 = format_str.format(num2)
        # print(num1, num2)
        add_flag, result = 0, ''
        for i in range(max_len - 1, -1, -1):
            temp = int(num1[i]) + int(num2[i]) + add_flag
            if temp >= 10:
                add_flag = temp // 10
                temp = temp % 10
            else:
                add_flag = 0
            result = str(temp) + result
        if add_flag > 0:
            result = str(add_flag) + result
        return result


def main():
    solution = Solution()
    tests = [
        ('111', '9'),
        ('999', '1'),
        ('111', '111')
    ]
    for num1, num2 in tests:
        print(solution.addStrings(num1, num2))


if __name__ == "__main__":
    main()
