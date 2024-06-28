#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            if fast.next:
                fast = fast.next
            else:
                head.next = None
                return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = fast
        return head


if __name__ == '__main__':
    s = Solution()
    # s.removeNthFromEnd(ListNode(1, ListNode(
    #     2, ListNode(3, ListNode(4, ListNode(5))))), 4)
    s.removeNthFromEnd(ListNode(1), 1)

# @lc code=end
