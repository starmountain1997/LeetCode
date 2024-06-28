#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_ptr = head
        nums = []
        for _ in range(left-1):
            left_ptr = left_ptr.next
        right_ptr = left_ptr
        for _ in range(right - left+1):
            nums.append(right_ptr.val)
            right_ptr = right_ptr.next
        nums.reverse()
        for n in nums:
            left_ptr.val = n
            left_ptr = left_ptr.next
        return head


if __name__ == '__main__':
    s = Solution()
    s.reverseBetween(ListNode(1, ListNode(
        2, ListNode(3, ListNode(4, ListNode(5, None))))), 2, 4)

# @lc code=end
