# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # TODO: 再看一遍
    def validate(self, root, ) -> int:
        if root is None:
            return True, 0
        balanced, left_height = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, right_height = self.validate(root.right)
        if not balanced:
            return False, 0
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = self.validate(root)
        return balanced


if __name__ == "__main__":
    s = Solution()
    s.isBalanced([-10, -3, 0, 5, 9])
