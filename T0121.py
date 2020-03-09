#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0121.py
@Time    :   2020/03/09 08:52:26
@Author  :   LaLaLa 
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        """
        循环暴力
        """
        if len(prices) <= 0:
            return 0
        result = 0
        for i in range(len(prices)):
            for j in range(len(prices)-1, i, -1):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    result = max(result, profit)
        return result


    def maxProfit2(self, prices):
        # 最低价格
        min_price= max(prices) if prices else 0
        # 最高利润
        max_profit = 0
        for price in prices:
            max_profit = max(price-min_price, max_profit)
            min_price = min(price, min_price)
        return  max_profit        


def main():
    solution = Solution()
    tests = [[7,1,5,3,6,4], [7,6,4,3,1], []]
    for test in tests:
        print(solution.maxProfit(test), "  ==>  ", solution.maxProfit2(test))


if __name__ == "__main__":
    main()