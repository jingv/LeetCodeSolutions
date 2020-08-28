#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   JingV
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


from collections import Counter


class Solution(object):
    def judgeCircle(self, moves):
        #return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
        counter = Counter(moves)
        return counter['U'] == counter['D'] and counter['L'] == counter['R']


def main():
    solution = Solution()
    tests = ['UD', 'LL']
    for moves in tests:
        print(solution.judgeCircle(moves))


if __name__ == "__main__":
    main()