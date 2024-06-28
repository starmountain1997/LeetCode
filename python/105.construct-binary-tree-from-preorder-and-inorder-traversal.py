#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:i+1], inorder[:i])
        right = self.buildTree(preorder[i + 1:], inorder[i+1:])
        root.left = left
        root.right = right
        return root


if __name__ == "__main__":
    s = Solution()
    s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# @lc code=end
