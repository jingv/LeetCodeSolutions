#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0332.py
@Time    :   2020/08/27 08:43:50
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


import collections


class Solution(object):
    def findItinerary(self, tickets):
        # 将数据组织为字典
        dir_tickets = collections.defaultdict(list)
        for ticket in tickets:
            dir_tickets[ticket[0]].append(ticket[1])
        # 将字典中的value降序排序
        for _ in dir_tickets:
            dir_tickets[_].sort(reverse=True)
        print(dir_tickets)
        # 组织答案
        result = []

        def dfs(pos):
            while dir_tickets[pos]:
                dfs(dir_tickets[pos].pop())
            result.append(pos)
        dfs('JFK')
        return result[::-1]


def main():
    solution = Solution()
    tests = [
        # [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
        # [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
        [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
    ]
    for test in tests:
        print(solution.findItinerary(test))


if __name__ == "__main__":
    main()
