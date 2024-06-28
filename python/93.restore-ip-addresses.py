#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def _restoreIpAddresses(self, s: str, res: str, points: int, res_list: List[str]):
        if points == 1:
            if len(s) > 0:
                if len(s) == 1:
                    res_list.append(res+"."+str(int(s)))
                elif s[0] != "0" and 10 <= int(s) <= 255:
                    res_list.append(res+"."+str(int(s)))
            return
        if len(s) >= 1:
            self._restoreIpAddresses(
                s[1:], res+"."+str(int(s[:1])), points-1, res_list)
        if len(s) >= 2 and s[0] != "0":
            self._restoreIpAddresses(
                s[2:], res+"."+str(int(s[:2])), points-1, res_list)
        if len(s) >= 3 and s[0] != "0" and 0 <= int(s[:3]) <= 255:
            self._restoreIpAddresses(
                s[3:], res+"."+str(int(s[:3])), points-1, res_list)

    def restoreIpAddresses(self, s: str) -> List[str]:
        res_list = []
        self._restoreIpAddresses(s, "", 4, res_list)
        res_list = [s[1:]for s in res_list]
        return res_list


if __name__ == "__main__":
    s = Solution()
    s.restoreIpAddresses("101023")

# @lc code=end
