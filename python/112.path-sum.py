# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.val == targetSum:
            if root.left is None and root.right is None:
                return True
        left_res = self.hasPathSum(root.left, targetSum-root.val)
        right_res = self.hasPathSum(root.right, targetSum-root.val)
        return left_res or right_res
