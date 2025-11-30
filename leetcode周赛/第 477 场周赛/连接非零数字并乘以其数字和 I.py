class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        n = n.replace("0","")
        if not n:
            return 0
        return int(n) * sum(map(int,n))