class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if the lengths match
        if len(s3) != len(s1) + len(s2):
            return False

        # Create a DP table
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True  # Base case

        # Fill the DP table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[len(s1)][len(s2)]