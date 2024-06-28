#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    # TODO:再做一遍
    # 搜索树的一个错误做法是：只判断左叶子节点比根节点小，右叶子节点比根节点大
    # 应该是左树的所有节点都比根节点小，右树的所有节点都比根节点大
    def _isValidBST(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self._isValidBST(root.left, min, root.val) and self._isValidBST(root.right, root.val, max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    solution = Solution()
    res = solution.generateTrees(5)
# @lc code=end

