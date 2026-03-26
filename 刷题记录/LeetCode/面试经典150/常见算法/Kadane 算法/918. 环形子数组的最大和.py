"""
https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
"""

"""
https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
"""
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], nums[i] + dp[i - 1]))
        return max(dp)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans1 = self.maxSubArray(nums)  # 先把情况一存储下来
        if ans1 < 0:  # 如果全是负数，直接返回即可
            return ans1
        # 然后判断第二种情况，就是利用环形特点
        # 代码是丑了点，常数是大了点，但好在思路清晰
        n = len(nums)
        sumL = [0]  # 正向前缀和
        for i in range(n):
            sumL.append(nums[i] + sumL[-1])
        sumR = [0]  # 逆向前缀和
        nums.reverse()
        for i in range(n):
            sumR.append(nums[i] + sumR[-1])
        maxL, maxR = [0], [0]  # 左边&右边的最大值
        for i in range(1, n + 1):
            maxL.append(max(sumL[i], maxL[-1]))
            maxR.append(max(sumR[i], maxR[-1]))
        ans2 = float("-inf")
        for i in range(n):
            ans2 = max(ans2, maxL[i] + maxR[n - i - 1])
        return max(ans1, ans2)


if __name__ == '__main__':
    s = Solution()
    nums = [-3, -2, -3]
    print(s.maxSubarraySumCircular(nums))
