from typing import List


class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        raw = [1]
        res = raw
        i = 1
        while i <= numRows:
            res = [1]*(i+1)
            j = 1
            while j < i:
                res[j] = raw[j-1]+raw[j]
                j += 1
            i += 1
            raw = res
        return res


if __name__ == "__main__":
    s = Solution()
    s.getRow(3)
