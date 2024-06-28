#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def _combinationSum(self, candidates: List[int], target: int, res: List, res_list: List[List[int]]) -> List[List[int]]:
        if target == 0:
            res_list.append(res)
            return
        for i, c in enumerate(candidates):
            if c <= target:
                self._combinationSum(
                    candidates[i:], target-c, res+[c], res_list)
            else:
                break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res_list = []

        self._combinationSum(candidates, target, [], res_list)
        return res_list


if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2, 3, 6, 7], 7)

# @lc code=end
