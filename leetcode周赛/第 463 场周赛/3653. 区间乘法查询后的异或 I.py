from functools import reduce
from operator import xor
from typing import List

mod = int(1e9+7)
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        for l,r,k,v in queries:
            for i in range(l,r + 1,k):
                nums[i] = (nums[i] * v) % mod
        return reduce(xor,nums)