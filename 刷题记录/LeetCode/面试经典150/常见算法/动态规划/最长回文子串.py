class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n+1):
            for i in range(n):
                if i + length - 1 >= n:
                    break
                j = i + length - 1
                if s[i] == s[j] and length == 2:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]

        for length in range(n, -1, -1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                if dp[i][j] == 1:
                    return s[i:j + 1]
        return ""


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("bb"))
