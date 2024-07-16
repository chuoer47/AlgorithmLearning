"""
https://www.acwing.com/problem/content/1016/
优化
预处理数组
"""


def LIS(weight: list, dp):
    """该方法的dp+1即为以这个元素为终止的上升子序列的长度"""
    if not weight:
        return 1
    n = len(weight)
    for i in range(n):
        for j in range(i):
            if weight[j] < weight[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp) + 1


n = int(input())
weight = list(map(int, input().strip().split(" ")))
dp_up = [0] * n
dp_down = [0] * n
LIS(weight, dp_up)
LIS(weight[::-1], dp_down)
res = 0
for i in range(n):
    res = max(res, dp_up[i] + dp_down[n - i - 1] + 1)
print(res)
