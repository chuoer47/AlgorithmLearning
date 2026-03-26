"""
https://www.acwing.com/problem/content/description/1019/
"""


def LIS(weight: list):
    n = len(weight)
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if weight[j] < weight[i]:
                dp[i] = max(dp[j] + 1, dp[i], 1)
    return max(dp) + 1

for _ in range(int(input())):
    n = int(input())
    weight = list(map(int, input().strip().split(" ")))
    print(max(LIS(weight), LIS(weight[::-1])))
