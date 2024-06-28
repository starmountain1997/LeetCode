#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        left_tree = self.buildTree(inorder[:i], postorder[:i])
        right_tree = self.buildTree(inorder[i+1:], postorder[i:-1])
        root.left = left_tree
        root.right = right_tree
        return root


# @lc code=end
