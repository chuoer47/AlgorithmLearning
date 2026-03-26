class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        cnts = Counter()
        cntt = Counter()
        for i in range(0,n,n//k):
            cnts[s[i:i+n//k]] += 1
            cntt[t[i:i+n//k]] += 1
        return cnts == cntt