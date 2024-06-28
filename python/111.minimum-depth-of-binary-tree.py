#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_minimal_depth = self.minDepth(root.left)
        right_minimal_depth = self.minDepth(root.right)
        if left_minimal_depth == 0 or right_minimal_depth == 0:  # TODO: 这一步很关键
            return left_minimal_depth+right_minimal_depth+1
        return min(left_minimal_depth, right_minimal_depth)+1

# @lc code=end
