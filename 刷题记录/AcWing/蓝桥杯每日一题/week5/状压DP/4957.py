"""
https://www.acwing.com/problem/content/4960/
"""
from math import inf

cycle = int(input())
for _ in range(cycle):
    n = int(input())
    lst = [list(map(int, input().split(" "))) for _ in range(n)]
    f = [inf] * (1 << n)
    f[0] = 0
    for i in range(1 << n):
        for j in range(n):
            if (1 << j) > i:  # 剪枝
                break
            if i >> j & 1:
                t, d, l = lst[j]
                pre = i - (1 << j)
                if t >= f[pre]:
                    f[i] = min(f[i], t + l)
                else:
                    if t + d >= f[pre]:
                        f[i] = min(f[i], f[pre] + l)
    if f[-1] != inf:
        print("YES")
    else:
        print("NO")
