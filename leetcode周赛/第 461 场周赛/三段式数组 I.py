from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        def isUp(nums):
            n = len(nums)
            for i in range(1, n):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        def isDown(nums):
            n = len(nums)
            for i in range(1, n):
                if nums[i] >= nums[i - 1]:
                    return False
            return True

        n = len(nums)
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                a = nums[: p + 1]
                b = nums[p: q + 1]
                c = nums[q:]
                if isUp(a) and isDown(b) and isUp(c):
                    return True
        return False
