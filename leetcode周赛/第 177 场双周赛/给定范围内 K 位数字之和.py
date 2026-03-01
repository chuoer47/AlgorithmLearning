class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod = int(1e9 + 7)
        return sum(range(l, r + 1)) * (pow(10, k, mod) - 1) * pow(9, -1, mod) % mod * pow(r - l + 1, k - 1, mod) % mod
