"""
https://www.acwing.com/problem/content/1016/
纯暴力打法
TLE
"""


def LIS(weight: list):
    if not weight:
        return 1
    n = len(weight)
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if weight[j] < weight[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp) + 1

n = int(input())
weight = list(map(int, input().strip().split(" ")))
res = 0
for i in range(n):
    res = max(res, LIS(weight[:i]+[weight[i]]) + LIS(weight[-1:i:-1]+[weight[i]])-1)
print(res)
