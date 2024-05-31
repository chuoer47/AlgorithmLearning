"""
https://loj.ac/p/10147
考虑按照圆形排列的情况!!!
"""
from math import inf

n = int(input().strip())
lst = list(map(int, input().strip().split(" ")))
# 直接简单粗暴的重复
n = 2 * n
lst = lst * 2
# 前缀和
sum_lst = lst.copy()
for i in range(1, n):
    sum_lst[i] = sum_lst[i] + sum_lst[i - 1]
# 初始化数组
dp_min = [[inf] * n for _ in range(n)]
dp_max = [[0] * n for _ in range(n)]
for i in range(n):
    dp_min[i][i] = 0
# 区间DP
for length in range(1, n):
    for i in range(n):
        j = min(i + length, n - 1)
        for k in range(i, j):
            # print(i, j, k)
            dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j] + sum_lst[j] - sum_lst[i] + lst[i])
            dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j] + sum_lst[j] - sum_lst[i] + lst[i])
res1 = inf
res2 = -inf
for i in range(n // 2):
    res1 = min(res1, dp_min[i][i + n // 2 - 1])
    res2 = max(res2, dp_max[i][i + n // 2 - 1])
print(res1)
print(res2)
