from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appear_once = set()
        appear_twice = set()
        for n in nums:
            if n in appear_once:
                appear_once.remove(n)
                appear_twice.add(n)
            elif n in appear_twice:
                appear_twice.remove(n)
            else:
                appear_once.add(n)
        return list(appear_once)[0]


if __name__ == "__main__":
    pass
