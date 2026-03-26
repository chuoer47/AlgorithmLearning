from functools import reduce
from typing import List

mod = 10**9 + 7


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        if all(x == nums[0] for x in nums):
            return 1

        orn = reduce(lambda x, y: x | y, nums)
        n = orn.bit_length()
        u = 1 << n

        def eq(orn):
            # 返回或等于orn的子序列数量

            dp = [0] * u  # dp[x]表示x子集的数目
            for x in nums:
                dp[x] += 1

            for i in range(n):
                bit = 1 << i
                if orn & bit == 0:
                    continue
                for x in range(u):
                    if x & bit == 0:
                        continue
                    dp[x] += dp[x ^ bit]
            ans = 0
            sub = orn
            while True:
                tmp = pow(2, dp[sub], mod)
                cnt = (orn ^ sub).bit_count()
                sign = 1 if cnt % 2 == 0 else -1
                ans = (ans + sign * tmp) % mod
                if sub == 0:
                    break
                sub = (sub - 1) & orn
            return ans

        all_sub = pow(2, len(nums), mod)  # 所有子序列的个数
        invalid = eq(orn)

        return (all_sub - invalid) % mod
