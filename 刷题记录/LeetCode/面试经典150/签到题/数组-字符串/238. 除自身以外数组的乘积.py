from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        num_zero = nums.count(0)
        if num_zero >= 2:
            return answer
        elif num_zero == 1:
            p = nums.index(0)
            t = 1
            for i in nums:
                if i != 0:
                    t *= i
            answer[p] = t
        else:
            t = 1
            for i in nums:
                t *= i
            for i in range(n):
                answer[i] = t // nums[i]
        return answer
