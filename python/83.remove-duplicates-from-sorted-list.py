#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while slow is not None and fast is not None:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return head


if __name__ == "__main__":
    solution = Solution()
    solution.climbStairs(44)

# @lc code=end

