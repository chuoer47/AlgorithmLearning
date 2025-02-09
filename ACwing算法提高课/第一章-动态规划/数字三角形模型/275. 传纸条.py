"""
https://www.acwing.com/problem/content/277/
和方格取数很像
"""

m, n = map(int, input().split(" "))
weight = [list(map(int, input().strip().split(" "))) for _ in range(m)]

dp = [[[0] * (m + 1)
       for _ in range(m + 1)]
      for _ in range(m + n + 1)]

# 以走的步数(k)先遍历
for k in range(2, m + n + 1):  # 从2开始是因为(1,1)坐标出发，1+1=2，到(m,n)
    for i1 in range(1, m + 1):
        for i2 in range(1, m + 1):
            j1, j2 = k - i1, k - i2
            if 1 <= j1 <= n and 1 <= j2 <= n:
                t = weight[i1-1][j1-1]
                if i1 != i2:
                    t += weight[i2-1][j2-1]
                dp[k][i1][i2] = max(dp[k][i1][i2],
                                    dp[k - 1][i1 - 1][i2 - 1] + t,
                                    dp[k - 1][i1][i2 - 1] + t,
                                    dp[k - 1][i1 - 1][i2] + t,
                                    dp[k - 1][i1][i2] + t,
                                    )

print(dp[m+n][m][m])
