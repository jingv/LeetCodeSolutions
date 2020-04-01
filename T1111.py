#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0111.py
@Time    :   2020/04/01 09:26:41
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    # def maxDepthAfterSplit(self, seq: str[]) -> List[int]:
    def maxDepthAfterSplit(self, seq):
        # 思想：只要保证两个连续的((或))不是分到同一个组内即可
        # 执行用时 :48 ms, 在所有 Python3 提交中击败了87.74%的用户
        # 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了16.67%的用户
        ans = [0]
        for i in range(1, len(seq)):
            ans.append(ans[i - 1]) if seq[i] != seq[i - 1] else ans.append(1 - ans[i - 1])
        return ans


def main():
    tests = ["(()())", "()(())()"]
    # output = [ [0,1,1,1,1,0], [0,0,0,1,1,0,1,1] ]
    solution = Solution()
    for test in tests:
        print(solution.maxDepthAfterSplit(test))


if __name__ == "__main__":
    main()
