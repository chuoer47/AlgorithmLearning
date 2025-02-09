"""
https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
第一种思路：
直接排序，取中位数
第二种思路：
boyer-moore算法
 假设你在投票选人 如果你和候选人（利益）相同，你就会给他投一票（count+1），
 如果不同，你就会踩他一下（count-1）当候选人票数为0（count=0）时，就换一个候选人，
 但因为和你利益一样的人占比超过了一半 不论换多少次 ，最后留下来的都一定是个和你（利益）相同的人。
"""

from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[min(len(nums)-1,len(nums)//2)]
#

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = -1
        for n in nums:
            if cnt == 0:
                candidate = n
            if candidate == n:
                cnt += 1
            else:
                cnt -= 1
        return candidate
