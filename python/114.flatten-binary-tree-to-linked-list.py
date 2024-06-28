#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p = root
        while p is not None:
            if p.left and p.right:
                tmp = p.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = p.right
                p.right, p.left = p.left, None
            elif not p.right and p.left:
                p.right, p.left = p.left, None
            p = p.right


if __name__ == '__main__':
    s = Solution()
    s.flatten(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
              TreeNode(5, None, TreeNode(6))))

# @lc code=end
