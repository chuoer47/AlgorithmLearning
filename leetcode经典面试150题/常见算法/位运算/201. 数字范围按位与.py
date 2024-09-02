"""
https://leetcode.cn/problems/bitwise-and-of-numbers-range/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for s in zip(*strs):
            s_set = set(s)
            if len(s_set) == 1:
                res += s[0]
            else:
                break
        return res

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        s_l = bin(left)
        s_r = bin(right)
        if len(s_l) != len(s_r):
            return 0
        t = self.longestCommonPrefix([s_l, s_r])
        t = t + "0" * (len(s_l) - len(t))
        return int(t, 2)
