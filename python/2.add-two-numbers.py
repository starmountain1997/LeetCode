#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        l1_cursor = l1
        l2_cursor = l2
        res = ListNode(0, None)
        res_cursor = res

        while l1_cursor is not None and l2_cursor is not None:
            val = l1_cursor.val + l2_cursor.val + c
            if val >= 10:
                c = 1
                val = val - 10
            res_cursor.val = val
            res_cursor.next = ListNode(0, None)
            l1_cursor = l1_cursor.next
            l2_cursor = l2_cursor.next
            res_cursor = res_cursor.next
        if l1_cursor is not None:
            res_cursor.next=l1_cursor
        elif l2_cursor is not None:
            res_cursor.next=l2_cursor
        return res


if __name__ == "__main__":
    s = Solution()
    l13 = ListNode(3, None)
    l12 = ListNode(4, l13)
    l11 = ListNode(2, l12)
    l23 = ListNode(4, None)
    l22 = ListNode(6, l23)
    l21 = ListNode(5, l22)

    s.addTwoNumbers(l11, l21)


# @lc code=end
