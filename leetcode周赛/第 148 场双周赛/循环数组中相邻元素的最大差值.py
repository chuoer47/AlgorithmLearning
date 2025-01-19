from cmath import inf
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = -inf
        n = len(nums)
        for i in range(n):
            ans = max(ans,abs(nums[i]-nums[i-1]))
        return ans

