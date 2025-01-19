from cmath import inf
from typing import List


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        def valid(pair1, pair2):
            return pair1[0] != pair1[1] and pair2[0] != pair2[1] and pair1[0] != pair2[0] and pair1[1] != pair2[1]

        match = [(i, j) for i in range(3) for j in range(3)]

        i, j = 0, n - 1
        dp = [0] * 9
        while i < j:
            ndp = [inf] * 9
            for x in range(9):
                for y in range(9):
                    if valid(match[x], match[y]):
                        ndp[x] = min(ndp[x], dp[y] + cost[i][match[x][0]] + cost[j][match[x][1]])
            dp = ndp
            i += 1
            j -= 1
        return min(dp)
