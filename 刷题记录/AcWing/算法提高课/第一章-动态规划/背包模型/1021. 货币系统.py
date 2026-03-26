"""
https://www.acwing.com/problem/content/1023/

参考1023.买书
"""

n,m = map(int,input().split(" "))
prices = [int(input()) for _ in range(n)]

dp = [0] * (m + 10)
dp[0] = 1
for p in prices:
    for i in range(p, m + 1):
        dp[i] += dp[i - p]
print(dp[m])
