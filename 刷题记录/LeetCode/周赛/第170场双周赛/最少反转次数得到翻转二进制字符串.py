class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        rs = s[::-1]
        return sum(s[i] != rs[i] for i in range(len(s)))