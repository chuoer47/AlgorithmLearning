class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        s = set(s)
        ans = -inf
        for a in s:
            for b in s:
                if cnt[a] % 2 == 0 and cnt[b] % 2 == 1:
                    ans = max(ans, cnt[b] - cnt[a])
        return ans
