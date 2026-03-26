"""
https://www.acwing.com/problem/content/733/
"""
from math import inf

# 数据录入
n = int(input())
w = [list(map(int, input().strip().split(" "))) for i in range(n)]

# 初始化
f = [[inf] * n for _ in range(1 << n)]
f[1][0] = 0  # 开始出发为0

# 状压DP
for st in range(1, 1 << n, 2):  # 优化常数，因为必须要经过第一个城市
    for j in range(0, n):
        if (1 << j) > st:
            break
        if not ((st >> j) & 1):  # 优化，只算有用的状态
            continue
        for k in range(0, n):
            if ((st - (1 << j)) >> k) & 1:  # k存在
                f[st][j] = min(f[st - (1 << j)][k] + w[k][j], f[st][j])

# 求解答案
res = inf
st = ((1 << n) - 1)
for i in range(0, n):
    res = min(f[st][i] + w[i][0], res)

print(res)
