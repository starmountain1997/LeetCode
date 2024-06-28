#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = [[root]]
        while len(res[-1]) != 0:
            l = []
            for n in res[-1]:
                if n.left is not None:
                    l.append(n.left)
                if n.right is not None:
                    l.append(n.right)
            res.append(l)
        if len(res[-1]) == 0:
            res.pop()
        res = [[n.val for n in l] for l in res]
        return res


if __name__ == '__main__':
    s = Solution()
    s.levelOrder(TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), None))

# @lc code=end
