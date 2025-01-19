from functools import cache
from typing import List

max_n = int(1e5 + 1)
fac = [1] * (max_n + 1)
facinv = [1] * (max_n + 1)

MAX_NUM = int(1e9 + 7)
for i in range(1, max_n + 1):
    fac[i] = fac[i - 1] * i % MAX_NUM
    # python自带快速幂
    facinv[i] = pow(fac[i], MAX_NUM - 2, MAX_NUM)


def myComb(n, m):
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n - m] % MAX_NUM


@cache
def sumComb(n, t):
    return sum(myComb(n, j) for j in range(0, t + 1)) % MAX_NUM


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = int(1e9 + 7)
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            t = min(k - 1, n - i - 1)
            # ans += nums[i] * sum(myComb(n - i - 1, j) for j in range(0, t + 1)) % mod
            ans += nums[i] * sumComb(n - i - 1, t)
            ans %= mod
        for i in range(n - 1, -1, -1):
            t = min(k - 1, i)
            # ans += nums[i] * sum(myComb(i, j) for j in range(0, t + 1)) % mod
            ans += nums[i] * sumComb(i, t)
            ans %= mod
        return ans % mod
