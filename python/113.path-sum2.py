# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _pathSum(self, root: Optional[TreeNode], targetSum: int, path: List, res: List[List]) -> List[List[int]]:
        if root is None:
            return
        if root.val == targetSum and root.left is None and root.right is None:
            path.append(root.val)
            res.append(path)
            return
        path.append(root.val)
        targetSum -= root.val
        self._pathSum(root.left, targetSum, path.copy(), res)
        self._pathSum(root.right, targetSum, path.copy(), res)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self._pathSum(root, targetSum, [], res)
        return res


if __name__ == "__main__":
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(r)
