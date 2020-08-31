#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0021.py
@Time    :   2020/05/01 23:25:57
@Author  :   JingV
@Version :   1.0
@Contact :   dllOoOllb.com
@Desc    :   None
'''

from Constructor.SomeNode import ListNode


class Solution:
    def mergeTwoList(self, l1, l2):
        result = ListNode(-1)
        result_cur = result
        l1_cur, l2_cur = l1, l2
        while l1_cur and l2_cur:
            if l1_cur.val > l2_cur.val:
                result_cur.next, l2_cur = l2_cur, l2_cur.next
            else:
                result_cur.next, l1_cur = l1_cur, l1_cur.next
            result_cur = result_cur.next
        result_cur.next = l1_cur if l1_cur else l2_cur
        return result.next


def Travel(l):
    cur = l
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    Travel(l1)
    Travel(l2)

    solution = Solution()
    Travel(solution.mergeTwoList(l1, l2))


if __name__ == "__main__":
    main()
