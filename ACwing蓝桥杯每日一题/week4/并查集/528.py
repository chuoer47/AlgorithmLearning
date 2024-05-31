"""
https://www.acwing.com/problem/content/530/
"""

# 找父节点
def find_father(x: int):
    if par[x] == x:
        return x
    par[x] = find_father(x)  # 路径压缩
    return par[x]


# 合并
def unite(x: int, y: int):
    fx = find_father(x)
    fy = find_father(y)
    if fx == fy:
        return
    else:
        par[fx] = fy


res = []
t = int(input())
for _ in range(t):
    n, h, r = list(map(int, input().strip().split(" ")))
    lst = [[0, 0, 0]] + [list(map(int, input().strip().split(" "))) for _ in range(n)]
    par = [i for i in range(n + 2)]  # 集合
    for i in range(1, n + 1):
        x, y, z = lst[i]
        if z <= r:
            # 注意这里的顺序，大的在前，小的在后
            unite(i, 0)
        if z + r >= h:
            unite(n + 1, i)
    for i in range(1, n + 1):
        for j in range(1, i):
            x1, y1, z1 = lst[i]
            x2, y2, z2 = lst[j]
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 <= (2 * r) ** 2:
                unite(i, j)
    if find_father(n + 1) == find_father(0):
        res.append("Yes")
    else:
        res.append("No")
for i in res:
    print(i)
