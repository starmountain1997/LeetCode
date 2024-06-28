#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        tail = head.next
        tail_pre = head
        while tail.next:
            tail_pre = tail_pre.next
            tail = tail.next
        tmp = head.next
        tmp_pre = head
        while not tmp_pre.val <= tail.val <= tmp.val:
            tmp = tmp.next
            tmp_pre = tmp_pre.next


if __name__ == "__main__":
    s = Solution()
    s.insertionSortList(ListNode(4, ListNode(
        2, ListNode(1, ListNode(3, ListNode(0))))))

# @lc code=end
