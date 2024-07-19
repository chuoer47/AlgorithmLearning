"""
https://www.acwing.com/problem/content/8/

参考1022. 宠物小精灵之收服.py的代码即可
"""

n, v, m = map(int, input().strip().split(" "))
n, m, k = v, m, n
lst = [list(map(int, input().strip().split(" "))) for _ in range(k)]
dp = [[0] * (m + 10) for _ in range(n + 10)]  # dp能捕捉的最多的宝可梦
for c, r, w in lst:
    for i in range(n, c - 1, -1):
        for j in range(m, r - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - c][j - r] + w)

most_num = dp[n][m]
print(most_num)
