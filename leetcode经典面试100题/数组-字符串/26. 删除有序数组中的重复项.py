"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tem = list(set(nums))
        tem.sort()
        nums[:len(tem)] = tem
        return len(tem)
