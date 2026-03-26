from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 前后缀分解的经典题目
        n = len(nums)
        left = [1]
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
        right = [1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right.append(right[-1] + 1)
            else:
                right.append(1)
        right = right[::-1]
        ans = max(right)
        for i in range(n):
            if i - 2 >= 0 and nums[i] >= nums[i - 2]:
                ans = max(ans, left[i - 2] + right[i] + 1)
            if right[i] + i < n or i > 0:
                ans = max(ans, right[i] + 1)
        return ans
