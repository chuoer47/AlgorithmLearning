"""
https://www.acwing.com/problem/content/93/
"""
from math import inf

n = int(input())
w = [list(map(int, input().split(" "))) for _ in range(n)]
f = [[inf] * n for _ in range(1 << n)]
f[1][0] = 0  # 初始化
# DP
for i in range(1, 1 << n, 2):
    for j in range(n):
        if (1 << j) - 1 > i:  # 剪枝
            break
        if not ((i >> j) & 1):  # 第j位不为1
            continue
        for k in range(n):
            if ((i - (1 << j)) >> k) & 1:  # 第k位不重，而且存在
                f[i][j] = min(f[i - (1 << j)][k] + w[k][j], f[i][j])
print(f[-1][-1])
