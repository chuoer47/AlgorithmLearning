from bisect import *
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # 枚举最小值
        nums.sort()
        n = len(nums)
        ans = n - 1
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            minn = nums[i]
            maxn = nums[i] * k
            p = bisect_right(nums, maxn)
            ans = min(ans, i + n - p)
        return ans
