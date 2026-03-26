"""
https://www.acwing.com/problem/content/description/4960/
尝试状态压缩
"""
from math import inf

res = []
t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split(" "))) for _ in range(n)]
    # 状态dp
    dp = [inf] * (1 << n)
    dp[0] = 0
    for i in range(1, 1 << n):
        for j in range(0, n):
            t, d, l = lst[j]
            if i >> j & 1:  # 存在
                last = dp[i - (1 << j)]
                if last <= t + d:
                    dp[i] = min(dp[i], max(last, t) + l)
    # print(dp)
    flag = dp[(1 << n) - 1] != inf
    if flag:
        res.append("YES")
    else:
        res.append("NO")
# 输出结果
for i in range(len(res)):
    print(res[i])
