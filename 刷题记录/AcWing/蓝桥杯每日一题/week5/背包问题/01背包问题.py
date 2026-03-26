"""
https://www.acwing.com/problem/content/2/
"""

n, v = map(int, input().split(" "))
lst = [[0, 0]] + [list(map(int, input().split(" "))) for _ in range(n)]  # 方便下标操作
dp = [[0] * (v + 10) for _ in range(n + 10)]  # 构建数组
# 动态规划
for i in range(1, n + 1):
    vi, wi = lst[i]  # 取值
    for j in range(1, v + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= vi:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - vi] + wi)
print(dp[n][v])
