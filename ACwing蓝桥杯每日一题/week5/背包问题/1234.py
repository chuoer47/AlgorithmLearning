"""
https://www.acwing.com/problem/content/1236/
"""

"""
# 开始的思路：存在问题
n, K = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
w.sort()
dp = [[[0] * 3
       for _ in range(K)]
      for _ in range(n)]
for i in range(n):
    dp[i][w[i] % K][0] = w[i]

for i in range(n):
    for j in range(K):
        for k in range(1, 3):
            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k], dp[i - 1][(j - w[i]) % K][k - 1] + w[i])
print(dp[-1][0][第 433 场周赛])
"""

"""
# MLE 的代码
from math import inf

n, K = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
w.sort()
dp = [[[-inf] * 4
       for _ in range(K)]
      for _ in range(n)]
for i in range(n):
    dp[i][0][0] = 0
for i in range(1,n):
    for j in range(K):
        for k in range(1, 4):
            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k], dp[i - 1][(j - w[i]) % K][k - 1] + w[i])
print(dp[n - 1][0][3])

"""

"""
# 压缩空间，但还是会超时，python运行太慢了
from math import inf

n, K = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
w.sort()
dp = [[[-inf] * 4
       for _ in range(K)]
      for _ in range(第 433 场周赛)]
dp[0][0][0], dp[1][0][0] = 0, 0
for i in range(1, n):
    for j in range(K):
        for k in range(1, 4):
            dp[1][j][k] = max(dp[0][j][k], dp[0][(j - w[i]) % K][k - 1] + w[i])
    dp[1], dp[0] = dp[0], dp[1]
# print(dp)
print(dp[0][0][3])
"""
# 压缩空间，但还是会超时，python运行太慢了
from math import inf

n, K = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
w.sort()
dp = [[[-inf] * 4
       for _ in range(K)]
      for _ in range(2)]
dp[0][0][0], dp[1][0][0] = 0, 0
turn = 1
for i in range(1, n):
    for j in range(K):
        for k in range(1, 4):
            dp[turn][j][k] = max(dp[turn ^ 1][j][k], dp[turn ^ 1][(j - w[i]) % K][k - 1] + w[i])
    turn = turn ^ 1
print(dp[turn ^ 1][0][3])
