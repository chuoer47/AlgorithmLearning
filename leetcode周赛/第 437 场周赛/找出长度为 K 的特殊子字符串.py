class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(0,n-k+1):
            now = s[i:i+k]
            cnt = Counter(now)
            if len(cnt.keys()) > 1:
                continue
            cc = s[i]
            if i - 1 >= 0 and cc == s[i-1]:
                continue
            if i+k < n and cc == s[i+k]:
                continue
            return True
        return False