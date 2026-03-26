from functools import cache
from math import comb


class Solution:
    @cache
    def nthSmallest(self, n: int, k: int) -> int:
        if n == 1:
            return (1 << k) - 1
        for high in range(k, 50 + 1):
            num = comb(high - 1, k - 1)
            if num >= n:
                return (1 << (high - 1)) | self.nthSmallest(n, k - 1)
            else:
                n -= num
