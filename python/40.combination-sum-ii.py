#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def _combinationSum2(self, candidates: List[int], target: int, res, res_list) -> List[List[int]]:
        if target == 0:
            res_list.append(res)
            return
        for i, c in enumerate(candidates):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if c <= target:
                self._combinationSum2(
                    candidates[i+1:], target-c, res+[c], res_list)
            else:
                break

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res_list = []
        self._combinationSum2(candidates, target, [], res_list)
        return res_list


if __name__ == "__main__":
    s = Solution()
    s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

# @lc code=end
