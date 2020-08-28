#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0491.py
@Time    :   2020/08/25 09:00:15
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def findSubsequences(self, nums):
        res = []

        def dfs(nums, temp):
            # 深度搜索遍历
            if len(temp) > 1:
                res.append(temp)
            curPres = {}
            for i in range(len(nums)):
                cur_num = nums[i]
                if cur_num in curPres:
                    continue
                if not temp or cur_num >= temp[-1]:
                    # 避免重复遍历, 重复的数字 当前层只遍历一次
                    curPres[cur_num] = 1
                    dfs(nums[i+1:], temp + [cur_num])
        dfs(nums, [])
        return res

    def findSubsequences_bfs(self, nums):
        res = []
        queue = [(nums, [])]
        while queue:
            source_nums, temp = queue.pop(0)
            if len(temp) > 1:
                res.append(temp)
            curPres = {}
            for i in range(len(source_nums)):
                cur_num = source_nums[i]
                if cur_num in curPres:
                    continue
                if not temp or cur_num >= temp[-1]:
                    curPres[cur_num] = 1
                    queue.append((source_nums[i+1:], temp + [cur_num]))
        return res


def main():
    solution = Solution()
    tests = [
        [4, 6, 7, 7]
    ]
    for test in tests:
        print(solution.findSubsequences(test))
        print(solution.findSubsequences_bfs(test))


if __name__ == "__main__":
    main()
