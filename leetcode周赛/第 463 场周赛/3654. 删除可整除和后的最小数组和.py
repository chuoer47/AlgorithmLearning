from cmath import inf
from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pi = list(accumulate(nums))
        rpi = list(accumulate(nums[::-1]))[::-1] + [0]
        map = defaultdict(lambda: inf)
        map[0] = 0
        ans = sum(nums)
        dp = [inf] * n + [0]
        for i, v in enumerate(nums):
            dp[i] = min(dp[i - 1] + v, map[pi[i] % k])
            map[pi[i] % k] = min(map[pi[i] % k], dp[i])
            ans = min(ans, dp[i] + rpi[i + 1])
        return ans
