# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _preorderTraversal(self, root: Optional[TreeNode], l: List) -> List[int]:
        if root is None:
            return
        l.append(root.val)
        if root.left is not None:
            self._preorderTraversal(root.left, l)
        if root.right is not None:
            self._preorderTraversal(root.right, l)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self._preorderTraversal(root, l)
        return l


if __name__ == "__main__":
    pass
