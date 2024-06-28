#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # TODO: 再写一遍
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))


if __name__ == "__main__":
    s = Solution()
    s.sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))


# @lc code=end
