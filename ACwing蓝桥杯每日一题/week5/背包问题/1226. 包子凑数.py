"""
https://www.acwing.com/problem/content/1228/
"""

# 抛弃数论知识，直接暴力求解
"""
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort() # 预处理加快速度
dp = [0] * 100000
dp[0] = 1
for i in range(1, len(dp)):
    for j in lst:
        if i >= j:
            dp[i] = max(dp[i], dp[i - j])
        else:
            break
res = len(dp) - sum(dp)
if res >= 100000//2:
    print("INF")
else:
    print(res)
"""

# 使用数论知识
from math import gcd

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()  # 预处理加快速度
g = 0
for i in lst:
    g = gcd(g, i)
if g != 1:
    print("INF")
    exit()
dp = [0] * 10000
dp[0] = 1
for i in range(1, len(dp)):
    for j in lst:
        if i >= j:
            dp[i] = max(dp[i], dp[i - j])
        else:
            break
print(len(dp) - sum(dp))
