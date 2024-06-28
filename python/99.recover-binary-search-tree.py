#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
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
    def _recoverTree(self, root: Optional[TreeNode], res: List) -> None:
        if root is None:
            return
        self._recoverTree(root.left, res)
        res.append(root)
        self._recoverTree(root.right, res)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self._recoverTree(root, res)
        res_val = [r.val for r in res]
        res_val.sort()
        for r, n in zip(res, res_val):
            if r.val != n:
                r.val = n


if __name__ == "__main__":
    s = Solution()
    s.recoverTree(TreeNode(3, TreeNode(9)))
# @lc code=end
