class Solution:
    def maxFreqSum(self, s: str) -> int:
        yuan = "aeiou"
        cnt = Counter(s)
        s1 = s2 = 0
        for x in cnt:
            if x in yuan:
                s1 = max(s1,cnt[x])
            else:
                s2 = max(s2,cnt[x])
        return s1 + s2