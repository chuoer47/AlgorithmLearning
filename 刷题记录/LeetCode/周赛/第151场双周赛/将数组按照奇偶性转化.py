from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        cnt = [0]*2
        for v in nums:
            cnt[v%2] += 1
        return [0]*cnt[0] + [1]*cnt[1]