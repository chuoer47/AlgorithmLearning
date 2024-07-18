"""
https://leetcode.cn/problems/permutations/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def per(nums,p):
            n = len(nums)
            if p==n:
                res.append(nums.copy())
            for i in range(p,n):
                nums[p],nums[i] = nums[i],nums[p]
                per(nums,p+1)
                nums[p],nums[i] = nums[i],nums[p]
        per(nums,0)
        return res

s = Solution()
print(s.permute([1,2,3]))