#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _inorderTraversal(self, root: Optional[TreeNode], l: List) -> List[int]:
        if root is None:
            return
        if root.left is not None:
            self._inorderTraversal(root.left, l)
        l.append(root.val)
        if root.right is not None:
            self._inorderTraversal(root.right, l)
        return l

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self._inorderTraversal(root, l)
        return l


if __name__ == "__main__":
    solution = Solution()
    solution.inorderTraversal()

# @lc code=end

