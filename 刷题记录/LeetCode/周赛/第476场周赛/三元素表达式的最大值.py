from cmath import inf
from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]


# class Solution:
#     def maximizeExpressionOfThree(self, nums: List[int]) -> int:
#         a, b, c = -inf, -inf, inf
#         for x in nums:
#             a, b = sorted([a, b, x])[1:]
#             c = min(x, c)
#         return a + b - c
