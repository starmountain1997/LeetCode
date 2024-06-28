from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appear_once = set()
        for n in nums:
            if n in appear_once:
                appear_once.remove(n)
            else:
                appear_once.add(n)
        return list(appear_once)[0]


if __name__ == "__main__":
    s = Solution()
    s.singleNumber([4, 1, 2, 1, 2])
