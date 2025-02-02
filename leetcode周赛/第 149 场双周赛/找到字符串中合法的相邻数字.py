class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        for i in range(0,n-1):
            a,b = s[i],s[i+1]
            if a == b:
                continue
            if cnt[a] == int(a) and cnt[b] == int(b):
                return a+b
        return ""