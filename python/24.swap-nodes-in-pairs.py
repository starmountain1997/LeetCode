#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast is not None:
            slow.val, fast.val = fast.val, slow.val
            if slow.next is not None and slow.next.next is not None:
                slow = slow.next.next
            else:
                break
            if fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
            else:
                break
        return head


if __name__ == "__main__":
    s = Solution()
    s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))


# @lc code=end
