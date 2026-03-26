"""
https://www.acwing.com/problem/content/1017/
"""

t = int(input())
for _ in range(t):
    r, c = map(int, input().split(" "))
    weight = [list(map(int, input().split(" "))) for _ in range(r)]
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + weight[i-1][j-1]
    print(dp[-1][-1])
