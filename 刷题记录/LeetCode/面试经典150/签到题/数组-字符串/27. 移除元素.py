"""
https://leetcode.cn/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tem = []
        for i in nums:
            if i != val:
                tem.append(i)
        k = len(tem)
        nums[:k] = tem
        return len(tem)


nums = [3, 2, 2, 3]
s = Solution()
k = s.removeElement(nums=nums, val=3)
print(nums, k)
