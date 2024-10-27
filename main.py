from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(k)]
        for i in range(n):
            dp[0][i] = stayScore[0][i]

        for i in range(1, k):
            for j in range(n):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + stayScore[i][j])
                for t in range(n):
                    dp[i][j] = max(dp[i][j], dp[i - 1][t] + travelScore[t][j])
        return max(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore(n=2, k=1, stayScore=[[1, 1]], travelScore=[[0, 1], [6, 0]]))
