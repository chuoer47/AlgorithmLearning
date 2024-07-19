"""
https://www.acwing.com/problem/content/280/
装满背包的DP
"""

n, m, = map(int, input().strip().split(" "))
nums = list(map(int, input().split(" ")))
dp = [0] * (m + 10)
dp[0] = 1

for p,num in enumerate(nums):
    for i in range(m,num-1,-1):
        dp[i] += dp[i-num]

print(dp[m])