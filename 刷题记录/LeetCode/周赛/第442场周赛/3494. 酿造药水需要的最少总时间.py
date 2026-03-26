from itertools import accumulate
from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        time = []  # 记录完成时间
        for i in range(n):
            time.append(skill[i] * mana[0])
        time = list(accumulate(time))
        for j in range(1, m):
            cost = [skill[i] * mana[j] for i in range(n)]
            cost = list(accumulate(cost))
            start_time = time[0]
            for i in range(n - 1):
                start_time = max(start_time, time[i + 1] - cost[i])
            time = [start_time + c for c in cost]
        return time[-1]