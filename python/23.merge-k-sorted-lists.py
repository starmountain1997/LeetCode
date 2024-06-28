#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # TODO: 复习最小堆
        heap = []
        root = res = ListNode(None)
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        while heap:
            res.next = ListNode(heapq.heappop(heap))
            res = res.next
        return root.next


if __name__ == "__main__":
    s = Solution()
    s.mergeKLists(
        [
            ListNode(1, ListNode(2, ListNode(3, ListNode()))),
            ListNode(2, ListNode(5, ListNode(8, ListNode()))),
            ListNode(3, ListNode(6, ListNode(9, ListNode()))),
            ListNode(4, ListNode(7, ListNode(10, ListNode()))),
        ]
    )

# @lc code=end
