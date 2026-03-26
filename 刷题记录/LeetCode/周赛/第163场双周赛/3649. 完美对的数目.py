from typing import List
from sortedcontainers import SortedList


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # 应该要排序
        # 假设1：按照|x|排序
        # 假设2：按照x排序
        # max(|a - b|, |a + b|) >= max(|a|, |b|) 打表发现恒成立
        # 按照假设1进行递减排序，进行相应的处理即可获得答案
        sl = SortedList()
        nums.sort(key=lambda x: abs(x), reverse=True)
        ans = 0
        for x in nums:
            xx = abs(x)
            left = sl.bisect_left(-2*xx)
            right = sl.bisect_right(2* xx)
            ans += right - left

            sl.add(x)
        return ans
