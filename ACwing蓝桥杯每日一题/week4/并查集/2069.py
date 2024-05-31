"""
https://www.acwing.com/problem/content/2071/
"""


# 找父节点
def find_father(x: int):
    if par[x] == x:
        return x
    par[x] = find_father(par[x]) # 路径压缩
    return par[x]


# 合并
def unite(x: int, y: int):
    fx = find_father(x)
    fy = find_father(y)
    if fx == fy:
        return
    else:
        par[fx] = fy


n, m = map(int, input().strip().split(" "))
operate = [list(map(int, input().strip().split(" "))) for _ in range(m)]
par = [i for i in range(n + 1)]
res = [0] * (n + 1)
for op in operate:
    op_type, x, y = op
    if op_type == 1:
        if x == y:
            continue
        unite(max(x, y), min(x, y))
    else:
        fx = find_father(x)
        for i in range(1, n + 1):
            if find_father(i) == fx:
                res[i] += y
    # print(par)
print(*res[1:])
