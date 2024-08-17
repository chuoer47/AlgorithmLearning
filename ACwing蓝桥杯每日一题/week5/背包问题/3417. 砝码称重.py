"""
https://www.acwing.com/problem/content/3420/
"""

n = int(input())
w = [0] + list(map(int, input().split(" ")))
w.sort()
sw = w.copy()  # 前缀和
for i in range(1, len(w)):
    sw[i] = sw[i] + sw[i - 1]
wn = sw[-1]  # w的总和
dp = [[0] * (wn + 3) for _ in range(n + 3)]
for i in range(n + 1):
    dp[i][0] = 1
for i in range(1, n + 1):
    for j in range(1, sw[i] + 1):
        dp[i][j] = max(dp[i-1][j],dp[i-1][abs(j-w[i])])
        if j + w[i] <= wn:
            dp[i][j] = max(dp[i][j], dp[i - 1][j + w[i]])
print(sum(dp[n]) - 1)
