class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p1, p2 = list(p.split("*"))
        idx1 = s.find(p1)
        if idx1 == -1:
            return False
        idx2 = s.find(p2, idx1 + len(p1))
        return idx2 != -1


s = Solution()
print(s.hasMatch(s="leetcode", p="ee*e"))
