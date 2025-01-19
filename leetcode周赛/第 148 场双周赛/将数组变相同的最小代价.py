from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        ans = sum(abs(i - j) for i, j in zip(arr, brr))
        modify = sum(abs(i - j) for i, j in zip(sorted(arr), sorted(brr))) + k
        return min(ans, modify)
