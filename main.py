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
                    ans = max(dp[i][j],ans)
                else:
                    dp[i][j] = 0
        return ans**2


if __name__ == '__main__':
    s = Solution()
    matix = [["1", "0", "1", "0", "0"],
             ["1", "0", "1", "1", "1"],
             ["1", "1", "1", "1", "1"],
             ["1", "0", "0", "1", "0"]]
    print(s.maximalSquare(matix))
