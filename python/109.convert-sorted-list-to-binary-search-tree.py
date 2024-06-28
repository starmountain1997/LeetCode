#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # TODO: 使用快慢指针解题
        l = 0
        tmp = head
        while tmp is not None:
            l += 1
            tmp = tmp.next
        if l == 0:
            return None
        elif l == 1:
            return TreeNode(head.val)
        m = l//2
        left = None
        root = head
        while m > 0:
            if left is None:
                left = root
            else:
                left = left.next
            root = root.next
            m -= 1
        left.next = None
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(root.next)
        root = TreeNode(root.val)
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    s = Solution()
    head = ListNode(-10, ListNode(-3, ListNode(0,
                    ListNode(5, ListNode(9, None)))))
    s.sortedListToBST(head)
# @lc code=end
