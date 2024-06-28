# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _sumNumbers(self, root: Optional[TreeNode], c: int, res: List) -> int:
        if root is None:
            return
        if root.left is None and root.right is None:
            res.append(c*10+root.val)
            return
        self._sumNumbers(root.left, c*10+root.val, res)
        self._sumNumbers(root.right, c*10+root.val, res)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        self._sumNumbers(root, 0, res)
        return sum(res)


if __name__ == "__main__":
    pass
