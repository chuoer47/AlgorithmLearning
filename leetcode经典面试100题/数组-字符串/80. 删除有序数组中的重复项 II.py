"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pivot = 0
        pre = nums[0]
        cnt = 0
        for i in range(0, len(nums)):
            if nums[i] == pre:
                cnt += 1
                if cnt <= 2:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot += 1
            else:
                cnt = 1
                pre = nums[i]
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        nums[:] = nums[:pivot+1]
        return pivot + 1
