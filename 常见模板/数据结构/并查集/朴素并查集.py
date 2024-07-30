n = 10000  # 这里可以自己改
par = [i for i in range(n + 1)]  # 初始化


def find_father(x):  # 并查集查找函数
    if par[x] == x:
        return x
    par[x] = find_father(par[x])  # 路径压缩
    return par[x]


def unite(x: int, y: int):  # 并查集组合函数
    fx = find_father(x)
    fy = find_father(y)
    if fx == fy:
        return
    else:
        par[fx] = fy


for i in range(1, n + 1):
    unite(i, int(input()))  # 根据条件添加关系，完成合并
