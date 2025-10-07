from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ans = mask = (1 << (n.bit_length())) - 1
        for i,x in enumerate(nums):
            if i != x:
                ans &= i
        return ans if ans < mask else 0