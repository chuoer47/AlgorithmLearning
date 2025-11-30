from collections import defaultdict
from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        odd = [x % 2 for x in nums]
        opi = list(accumulate(odd))
        pi = list(accumulate(nums, func=xor))
        # print(pi,opi)
        mapper = defaultdict(int)
        mapper[(0, 1)] = -1
        # pi[r] = pi[l];  2*opi[r] - r = 2*opi[l] - l => 找到两个满足条件的最小的l => 最长长度
        # pi[-1],2*opi[-1] - (-1) = -1 => (0,1)=-1
        ans = 0
        for r, x in enumerate(nums):
            target = (pi[r], 2 * opi[r] - r)
            # print(r,target)/
            if target in mapper:
                idx = mapper[target]
                ans = max(ans, r - idx)
            if target not in mapper:
                mapper[target] = r
        return ans

