from collections import defaultdict
from functools import reduce
from math import isqrt
from operator import xor
from typing import List

mod = int(1e9 + 7)


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        B = isqrt(q)
        diff = defaultdict(list)
        for l, r, k, v in queries:
            if k < B:
                if not diff[k]:
                    diff[k] = [1] * (n + k)
                diff[l] = diff[l] * v % mod
                r = r - (r - l) % k + k
                diff[r] = diff[r] * pow(v, -1, mod) % mod
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod
        for k, d in diff.items():
            for start in range(k):
                mul_d = 1
                for i in range(start, n, k):
                    mul_d = mul_d * d[i] % mod
                    nums[i] = nums[i] * mul_d % mod
        return reduce(xor, nums)
