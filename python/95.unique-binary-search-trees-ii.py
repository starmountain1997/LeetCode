#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
import itertools
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _generateTrees(self, num_list, d: Dict):
        if len(num_list) == 0:
            return [None]
        elif f"{num_list[-1]}/{num_list[-1]}" in d:
            return d[f"{num_list[-1]}/{num_list[-1]}"]
        elif len(num_list) == 1:
            return [TreeNode(num_list[0])]
        elif len(num_list) == 2:
            return [TreeNode(num_list[0], None, TreeNode(num_list[1])), TreeNode(num_list[1], TreeNode(num_list[0]), None)]

        res = []
        for i, n in enumerate(num_list):
            if len(num_list[:i]) == 0:
                left_trees = [None]
            elif f"{num_list[0]}/{num_list[i-1]}" in d:
                left_trees = d[f"{num_list[0]}/{num_list[i-1]}"]
            else:
                left_trees = self._generateTrees(num_list[:i], d)
            if len(num_list[i+1:]) == 0:
                right_trees = [None]
            elif f"{num_list[i+1]}/{num_list[-1]}" in d:
                right_trees = d[f"{num_list[i+1]}/{num_list[-1]}"]
            else:
                right_trees = self._generateTrees(num_list[i+1:], d)
            for l, r in itertools.product(left_trees, right_trees):
                res.append(TreeNode(n, l, r))
        d[f"{num_list[0]}/{num_list[-1]}"] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        d = dict()
        num_list = [i for i in range(1, n+1)]
        res = self._generateTrees(num_list, d)
        return res


class Solution1:
    def _generateTrees(self, num_list, ):
        if len(num_list) == 0:
            return [None]
        elif len(num_list) == 1:
            return [TreeNode(num_list[0])]
        elif len(num_list) == 2:
            return [TreeNode(num_list[0], None, TreeNode(num_list[1])), TreeNode(num_list[1], TreeNode(num_list[0]), None)]

        res = []
        for i, n in enumerate(num_list):
            left_trees = self._generateTrees(num_list[:i])
            right_trees = self._generateTrees(num_list[i+1:])
            for l, r in itertools.product(left_trees, right_trees):
                res.append(TreeNode(n, l, r))
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        num_list = [i for i in range(1, n+1)]
        res = self._generateTrees(num_list)
        return res


if __name__ == "__main__":
    solution = Solution()
    res = solution.generateTrees(5)

# @lc code=end

