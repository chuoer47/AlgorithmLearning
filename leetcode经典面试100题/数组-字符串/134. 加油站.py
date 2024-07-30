"""
https://leetcode.cn/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
太讨厌这题目了
明明贪心很好理解，代码不好写...
"""
from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasSize, costSize = len(gas), len(cost)
        minOil = gas[0] - cost[0]
        has = minOil
        pivot = 0
        for i in range(1, gasSize):
            has += gas[i] - cost[i]
            if has <= minOil:
                minOil = has
                pivot = i
        if has >= 0:
            return (pivot + 1) % gasSize
        return -1
