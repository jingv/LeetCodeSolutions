#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Interview16-11DivingBoardLcci.py
@Time    :   2020/07/08 10:48:47
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    def divingBoard(self, shorter, longer, k):
        if k == 0:
            # 特殊情况1： k == 0, return []
            return []
        if shorter == longer:
            # 特殊情况2： shorter == longer, return [shorter/longer * k]
            return [shorter * k]
        # 普通红情况：shorter < longer, 共有k+1种组合情况
        # 随着longer个数的增加，跳水板的总长度呈一元线性函数增加：
        # length = shorter * shorter_count + longer * (k - shorter_count) 因变量为shorter_count，其余为常数
        # 简化后为： length = longer * k + (shorter - longer) * shorter_count
        # 或：length = shorter * k + (longer - shorter) * longer_count
        result, all_shorter, diff = [], shorter * k, longer - shorter
        for longer_count in range(k + 1):
            result.append(all_shorter + diff * longer_count)
        return result


def main():
    solution = Solution()
    tests = [
        [1, 2, 3],
        [1, 2, 1],
    ]
    for shorter, longer, k in tests:
        print(solution.divingBoard(shorter, longer, k))


if __name__ == "__main__":
    main()
