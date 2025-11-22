"""
没做出来
"""

n, k = map(int, input().strip().split(" "))
s = "#" + input().strip()
dp = [0] * (n + 10)

for i in range(k, n + 1):
    if s[i] == s[i - k - 1]:
        dp[i] = max(dp[i], dp[i - k - 1] + k + 1, k + 1)
