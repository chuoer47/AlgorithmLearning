class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        ans = 0
        l, r = 0, 0
        dic = {}
        while r < n:
            if s[r] not in dic:
                dic[s[r]] = r
            else:
                l = max(l,dic[s[r]] + 1)
                dic[s[r]] = r
            ans = max(ans, r - l + 1)
            r += 1
        return ans

