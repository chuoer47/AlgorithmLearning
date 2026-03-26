"""
https://www.acwing.com/problem/content/1224/
"""
from math import inf

# 录入数据
s = input()
n = len(s)
# 初始化
dp = [[inf] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
# dp
for length in range(2, n + 1):
    for i in range(n):
        if i + length - 1 < n:
            j = i + length - 1
            # print(i, j)
            if s[i] == s[j]:
                if j-i == 1: # 特判
                    dp[i][j] = 0
                dp[i][j] = min(dp[i + 1][j - 1], dp[i][j])
            else:
                dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1, dp[i][j], dp[i + 1][j - 1] + 2)
# print(dp)
print(dp[0][n - 1])
