"""
https://www.acwing.com/problem/content/1014/
"""

def LIS(weight: list):
    n = len(weight)
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if weight[j] < weight[i]:
                dp[i] = max(dp[j] + 1, dp[i], 1)
    return max(dp) + 1

n = int(input())
weight = [list(map(int,input().strip().split(" "))) for _ in range(n)]
weight.sort(key=lambda x:x[0]) # 这个排序简直是点睛之笔
weight = [i[1] for i in weight]
print(LIS(weight))