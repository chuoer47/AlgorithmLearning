"""
https://www.acwing.com/problem/content/1018/
"""


def LIS_sum(weight: list):
    n = len(weight)
    dp = weight.copy()
    for i in range(n):
        for j in range(i):
            if weight[j] < weight[i]:
                dp[i] = max(dp[j] + weight[i], dp[i])
    return max(dp)


n = int(input())
weight = list(map(int, input().strip().split(" ")))
print(LIS_sum(weight))
