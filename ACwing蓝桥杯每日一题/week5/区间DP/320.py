"""
https://www.acwing.com/problem/content/322/
"""

# 数据录入
n = int(input())
lst = list(map(int, input().strip().split(" ")))
w = []
for i in range(n):
    t = (lst[i], lst[(i + 1) % n])
    w.append(t)
# 处理环形
w = w * 2
n = n * 2
# dp初始化
dp = [[0] * n for _ in range(n)]
for length in range(2, n + 1):
    for i in range(n):
        if i + length - 1 < n:
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = max(dp[i][j],
                               dp[i][k] + dp[k + 1][j] + w[i][0] * w[k][1] * w[j][1])

# 比较出最大的结果
res = -1
for i in range(n // 2):
    res = max(res, dp[i][i + n // 2 - 1])
print(res)
