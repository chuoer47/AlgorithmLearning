from heapq import heapify, heappop
from itertools import accumulate
from typing import List


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        # 最小堆更新
        tmp = hp
        score = 0
        n = len(damage)
        need = []
        vis = [0] * n
        pi = list(accumulate(damage))
        for i in range(n):
            hp -= damage[i]
            if hp >= requirement[i]:
                score += 1
                vis[i] = 1
            else:
                need.append([requirement[i] + pi[i], i])

        ans = 0
        hp = tmp
        heapify(need)
        for i in range(n):

            ans += score
            hp += damage[i]
            score -= vis[i]
            while need and need[0][0] <= hp:
                idx = need[0][1]
                if idx >= i + 1:
                    vis[need[0][1]] = 1
                    score += 1
                heappop(need)

        return ans
