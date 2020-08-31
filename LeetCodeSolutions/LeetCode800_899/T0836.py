#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0836.py
@Time    :   2020/03/18 08:59:35
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution:
    # def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    def isRectangleOverlap(self, rec1, rec2):
        # 反证法？
        # 假设矩形2固定，矩形1与矩形2不重叠，则矩形1在矩形2的四周，即上方，下方，左方，右方。当这些情况成立时，返回false，否则返回true
        # 执行用时 :52 ms, 在所有 Python3 提交中击败了10.00%的用户
        # 内存消耗 :13.4 MB, 在所有 Python3 提交中击败了5.88%的用户
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

    def isRectangleOverlap2(self, rec1, rec2):
        # 直接检查两个矩形是否有重叠可以转换为连个矩形的边，在x轴和y轴上的投影是否有交集
        # 当x轴上的投影满足条件min(rec1_x2, rec2_x2) > max(rec1_x1, rec2_x2)则有交集，y轴同理
        # 只要x轴 y轴上都存在重叠的边，那么矩形1与矩形2则重叠
        # 执行用时 :40 ms, 在所有 Python3 提交中击败了33.10%的用户
        # 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.88%的用户
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))


def main():
    tests = [([0, 0, 2, 2], [1, 1, 3, 3]), ([0, 0, 1, 1], [1, 0, 2, 1])]
    solution = Solution()
    for rec1, rec2 in tests:
        print(solution.isRectangleOverlap(rec1, rec2))


if __name__ == "__main__":
    main()
