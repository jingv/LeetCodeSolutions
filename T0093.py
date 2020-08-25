#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0093.py
@Time    :   2020/08/25 09:49:17
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def restoreIpAddress(self, s):
        queue = [(s, "")]
        result = []
        while queue:
            source_str, front_str = queue.pop(0)
            # 判断是否符合条件
            if front_str.count('.') == 3:
                if len(source_str) == 0:
                    continue
                elif source_str.startswith('0') and len(source_str) != 1:
                    continue
                elif 0 <= int(source_str) <= 255:
                    result.append(front_str + source_str)
                else:
                    continue
            # 组合
            temp = ''
            for i in range(len(source_str)):
                temp += source_str[i]
                if 0 < int(temp) <= 255:
                    queue.append((source_str[i+1:], front_str + temp + '.'))
                elif int(temp) == 0:
                    queue.append((source_str[i+1:], front_str + temp + '.'))
                    break
                else:
                    break
        return result


def main():
    solution = Solution()
    tests = [
        "25525511135",
        '0000',
        '1111',
        '010010',
        '101023',
        '00000',
    ]
    for test in tests:
        print(solution.restoreIpAddress(test))


if __name__ == "__main__":
    main()
