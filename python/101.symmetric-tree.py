#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    # TODO: runtime不达标
    def _isSymmetric(self, r, l):
        if r is None and l is None:
            return True
        if r is not None and l is not None and r.val == l.val:
            return self._isSymmetric(r.right, l.left) and self._isSymmetric(r.left, l.right)
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)


if __name__ == "__main__":
    s = Solution()
    s.isSymmetric()

# @lc code=end

