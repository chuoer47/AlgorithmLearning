"""
https://www.acwing.com/problem/content/1024/
"""

n, m, k = map(int, input().strip().split(" "))
lst = [list(map(int, input().split(" "))) for _ in range(k)]
dp = [[0] * (m + 10) for _ in range(n + 10)]  # dp能捕捉的最多的宝可梦
for c, r in lst:
    for i in range(n, c - 1, -1):
        for j in range(m, r - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - c][j - r] + 1)

most_num = dp[n][m-1]
cost = m
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if dp[i][j] == most_num:
            cost = min(cost, j)

if most_num==0:
    print(most_num,m)
else:
    print(most_num, m - cost)
