#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0043.py
@Time    :   2020/08/13 09:53:32
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def multiply(self, num1, num2):
        if not num1 or not num2:
            return
        sort_num = sorted([num1, num2], key=lambda i: len(i))
        result = '0'
        num_small, num_larger, times = sort_num[0], sort_num[1], ''
        # 取较小数字中的最后一个数字与较大数相乘
        for n_s in num_small[::-1]:
            # 与较大数相乘, temp_result保存结果
            # 如果较小数字中的最后一位为0， 更改倍数
            if n_s == '0':
                times += '0'
                continue
            # 其余情况计算相乘
            flag, temp_result = 0, ''
            for n_l in num_larger[::-1]:
                temp = int(n_s) * int(n_l) + flag
                if temp >= 10:
                    flag, temp = temp // 10, temp % 10
                else:
                    flag = 0
                temp_result = str(temp) + temp_result
            if flag > 0:
                temp_result = str(flag) + temp_result
            # print(temp_result)
            # 加上倍数
            temp_result += times
            # 更改倍数
            times += '0'
            # print("result = {}, temp_result = {}".format(result, temp_result))
            result = self.add(result, temp_result)
        return result

    def add(self, str1, str2):
        '''计算两个字符串的和'''
        max_len = max(len(str1), len(str2))
        format_str = "{:0>" + str(max_len) + "}"
        str1_ex = format_str.format(str1)
        str2_ex = format_str.format(str2)
        flag, result, cur_index = 0, '', -1
        while cur_index >= -max_len:
            temp = int(str1_ex[cur_index]) + int(str2_ex[cur_index]) + flag
            if temp >= 10:
                temp, flag = temp % 10, 1
            else:
                flag = 0
            result = str(temp) + result
            cur_index = cur_index - 1
        return str(flag) + result if flag == 1 else result


def main():
    solution = Solution()
    tests = [
        ['999', '9999'],
        # ['999', '1'],
        # ['123', '1'],
        # ['2', '3'],
        # ['123', '456'],
    ]
    for num1, num2 in tests:
        print(solution.multiply(num1, num2))


if __name__ == "__main__":
    main()
