class Solution:
    def residuePrefixes(self, s: str) -> int:
        ss = set()
        ans = 0
        for i, v in enumerate(s):
            ss.add(v)
            if (i + 1) % 3 == len(ss):
                ans += 1
            if len(ss) >= 3:
                return ans
        return ans