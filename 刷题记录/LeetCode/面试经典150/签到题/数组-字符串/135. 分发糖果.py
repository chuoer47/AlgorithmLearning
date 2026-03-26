"""
https://leetcode.cn/problems/candy/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_l = [1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candy_l[i] = candy_l[i-1]+1
        candy_r = [1]*n
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy_r[i] = candy_r[i+1]+1
        candy = 0
        for i in range(n):
            candy+=max(candy_l[i],candy_r[i])
        return candy