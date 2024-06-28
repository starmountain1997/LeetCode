#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        res = [[n.val for n in l]for l in res]
        res = res[::-1]
        return res


# @lc code=end
