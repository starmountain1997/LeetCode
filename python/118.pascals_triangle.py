from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        i = 1
        while i < numRows:
            res.append([1]*(i+1))
            j = 1
            while j < i:
                res[i][j] = res[i-1][j-1]+res[i-1][j]
                j += 1
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.generate(5)
