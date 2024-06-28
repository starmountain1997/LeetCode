#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    res = float("-inf")

    def _maxPathSum(self, root: Optional[TreeNode]) -> int:
        # TODO: 再做一遍
        if root is None:
            return 0
        left_max = self._maxPathSum(root.left)
        if left_max < 0:
            left_max = 0
        right_max = self._maxPathSum(root.right)
        if right_max < 0:
            right_max = 0
        this_max = root.val + left_max + right_max
        self.res = max(this_max, self.res)
        return root.val + max(left_max, right_max)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._maxPathSum(root)
        return self.res


if __name__ == '__main__':
    s = Solution()
    s.maxPathSum(TreeNode(1, TreeNode(2, None), TreeNode(3, None)))

# @lc code=end
