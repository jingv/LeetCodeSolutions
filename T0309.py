#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0309.py
@Time    :   2020/07/10 09:20:27
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def maxProfit(self, prices):
        if not prices:
            return 0
        # 第i天拥有股票，最大收益为f[i][0]
        # 第i天不拥有股票，处于冷冻期，最大收益为f[i][1]
        # 第i天不拥有股票，不处于冷冻期，最大收益为f[i][2]

        # 第i天拥有股票
        #   1. 股票可能是第i-1天就已经持有的，收益为f[i-1][0]
        #   2. 股票是第i天购入的，那么第i-1天为不拥有股票，不处于冷冻期，收益为f[i-1][2]
        # f[i][0] = max(f[i-1][0], f[i-1][2]-prices[i])

        # 第i天不拥有股票，处于冷冻期 == 第i-1天时拥有股票，并且在第i天卖出
        # f[i][1] = f[i-1][0] + prices[i]

        # 第i天不拥有股票，不处于冷冻期
        #   1. 第i-1天不拥有股票，处于冷冻期，收益为f[i-1][1]
        #   2. 第i-1天不拥有股票，不处于冷冻期，收益为f[i-1][2]
        # f[i][2] = max(f[i-1][1], f[i-1][2])

        # 最大收益为 max(f[n][0], f[n][1], f[n][2]) => 共有n天(n为天数，不是索引)
        # 因为在最后一天持有股票无法获取当前股票的收益，故最大收益可简化为max(f[n][1], f[n][2])

        days = len(prices)
        f = [[0 for _ in range(3)] for _ in range(days)]
        # 第1天拥有股票，只能是第1天购入的
        f[0][0] = -prices[0]

        for i in range(1, days):
            print(i)
            f[i][0] = max(f[i-1][0], f[i-1][2] - prices[i])
            f[i][1] = f[i-1][0] + prices[i]
            f[i][2] = max(f[i-1][1], f[i-1][2])

        print(f)
        return max(f[days-1][1], f[days-1][2])


def main():
    solution = Solution()
    tests = [
        [1, 2, 3, 0, 2]
    ]
    for test in tests:
        print(solution.maxProfit(test))


if __name__ == "__main__":
    main()
