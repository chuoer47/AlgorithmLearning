"""
https://leetcode.cn/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150

经典二维DP问题
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
                    ans = max(dp[i][j], ans)
                else:
                    dp[i][j] = 0
        return ans ** 2
