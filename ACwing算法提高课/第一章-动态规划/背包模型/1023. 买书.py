"""
https://www.acwing.com/problem/content/1025/

题解：
https://www.acwing.com/solution/content/52967/

总的来说是：
这是一道道的 完全背包问题 求解方案数的经典问题
"""

n = int(input())
prices = [10, 20, 50, 100]
dp = [0] * (n + 10)
dp[0] = 1
for p in prices:
    for i in range(p, n + 1):
        dp[i] += dp[i - p]
print(dp[n])
