from typing import List

from sortedcontainers import SortedList


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # 不等式变换的题目，好久没做过了。
        sl = SortedList([1])
        ans = 0
        p = 0
        for right, val in enumerate(nums):
            p += int(val == target)
            sl.add(2 * p - right)
            idx = sl.bisect_left(2 * p - right)
            ans += idx
        return ans
