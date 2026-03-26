from bisect import bisect_right
from typing import List


class Solution:
    def countStableSubarrays(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        left = []
        s = [0]
        start = 0
        for i, x in enumerate(nums):
            if i == n - 1 or x > nums[i + 1]:
                left.append(start)
                m = i - start + 1
                s.append(s[-1] + m * (m + 1) // 2)
                start = i + 1
        ans = []
        for l, r in queries:
            i = bisect_right(left, l)
            j = bisect_right(left, r) - 1
            if i > j:
                m = r - l + 1
                ans.append(m * (m + 1) // 2)
                continue
            m = left[i] - l
            m2 = r - left[j] + 1
            ans.append(m * (m + 1) // 2 + m2 * (m2 + 1) // 2 + (s[j] - s[i]))
        return ans
