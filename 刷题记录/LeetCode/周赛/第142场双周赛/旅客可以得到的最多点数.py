from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(n):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + stayScore[i - 1][j])
                for t in range(n):
                    dp[i][j] = max(dp[i][j], dp[i - 1][t] + travelScore[t][j])
        return max(dp[-1])
