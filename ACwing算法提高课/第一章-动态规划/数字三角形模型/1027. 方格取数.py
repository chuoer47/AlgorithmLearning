"""
https://www.acwing.com/problem/content/1029/

如果只是先走一条最优路线，然后标记为0，再走一条的方法明显是错误的。即贪心算法错误！

正确解法：
同时考虑两条路线dp[i1][j1][i2][j2]。
优化策略：只能向左或者向右，使用k代替j1,j2
"""

N = 11
weight = [[0] * N for _ in range(N)]
n = int(input())
while True:
    x, y, v = map(int, input().strip().split(" "))
    if x == 0 and y == 0 and v == 0:
        break
    weight[x][y] = v

dp = [[[0] * N
       for _ in range(N)]
      for _ in range(2 * N)]

# 以走的步数(k)先遍历
for k in range(2, 2 * n + 1):  # 从2开始是因为(1,1)坐标出发，1+1=2
    for i1 in range(1, n + 1):
        for i2 in range(1, n + 1):
            j1, j2 = k - i1, k - i2
            if 1 <= j1 <= n and 1 <= j2 <= n:
                t = weight[i1][j1]
                if i1 != i2:
                    t += weight[i2][j2]
                dp[k][i1][i2] = max(dp[k][i1][i2],
                                    dp[k - 1][i1 - 1][i2 - 1] + t,
                                    dp[k - 1][i1][i2 - 1] + t,
                                    dp[k - 1][i1 - 1][i2] + t,
                                    dp[k - 1][i1][i2] + t,
                                    )
print(dp[2 * n][n][n])
