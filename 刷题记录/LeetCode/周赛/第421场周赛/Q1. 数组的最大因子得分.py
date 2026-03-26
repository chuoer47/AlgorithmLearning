from math import gcd, lcm, inf
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def get(nums):
            if not nums:
                return 0
            lcmn = gcdn = nums[0]
            for num in nums:
                lcmn = lcm(num, lcmn)
                gcdn = gcd(num, gcdn)
            return lcmn * gcdn

        ans = get(nums)
        n = len(nums)
        for i in range(n):
            ans = max(ans, get(nums[:i] + nums[i + 1:]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore(nums=[3]))
