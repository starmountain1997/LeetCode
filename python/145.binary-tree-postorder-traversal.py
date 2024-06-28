# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _postorderTraversal(self, root: TreeNode, l: List):
        if root is None:
            return
        if root.left is not None:
            self._postorderTraversal(root.left, l)
        if root.right is not None:
            self._postorderTraversal(root.right, l)
        l.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self._postorderTraversal(root, l)
        return l


if __name__ == "__main__":
    pass
