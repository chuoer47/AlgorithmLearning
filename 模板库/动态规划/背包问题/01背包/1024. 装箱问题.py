"""
https://www.acwing.com/problem/content/1026/
"""

v = int(input())
n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [0]*(v+10)
for w in lst:
    for i in range(v,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+w)
print(v-dp[v])