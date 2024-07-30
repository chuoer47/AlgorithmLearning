"""
https://www.acwing.com/problem/content/259/

拓展并查集:https://www.cnblogs.com/yHan234/p/16473336.html
"""


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


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    par = [i for i in range(2 * n + 10)]  # 构造拓展并查集
    lst = [list(map(int, input().strip().split(" "))) for _ in range(m)]
    lst.sort(key=lambda x: x[2], reverse=True)  # 按照仇恨权值排序
    ans = 0  # 无仇恨发生为0
    for a, b, c in lst:
        if find_father(a) == find_father(b):
            ans = c
            break
        else:
            unite(a, b + n)  # 这简直是神迹操作
            unite(b, a + n)
    print(ans)
