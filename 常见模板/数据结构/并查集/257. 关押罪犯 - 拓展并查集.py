"""
https://www.acwing.com/problem/content/259/

拓展并查集:https://www.cnblogs.com/yHan234/p/16473336.html
"""


def find_father(x):
    """
    并查集的查找函数，用于寻找元素x所在集合的根节点

    采用路径压缩优化：在查找过程中，将x到根节点路径上的所有节点直接指向根节点，
    减少后续查找操作的时间复杂度。

    参数:
        x: 要查找根节点的元素

    返回:
        x所在集合的根节点
    """
    if par[x] == x:  # 若x是根节点，直接返回
        return x
    # 路径压缩：将x的父节点更新为根节点
    par[x] = find_father(par[x])
    return par[x]


def unite(x: int, y: int):
    """
    并查集的合并函数，用于将元素x和y所在的两个集合合并

    参数:
        x: 第一个元素
        y: 第二个元素
    """
    # 找到x和y各自的根节点
    fx = find_father(x)
    fy = find_father(y)
    if fx == fy:  # 若已在同一集合，无需合并
        return
    else:  # 否则将一个集合的根节点指向另一个集合的根节点
        par[fx] = fy


if __name__ == '__main__':
    # 读取输入：n表示元素数量，m表示关系数量
    n, m = map(int, input().strip().split(" "))
    # 初始化并查集数组，大小为2*n+10（拓展并查集，用于处理对立关系）
    # 下标范围足够容纳原元素和其对立元素（原元素i的对立元素可表示为i+n）
    par = [i for i in range(2 * n + 10)]
    # 读取m个关系，每个关系为[a, b, c]，表示a和b之间的仇恨值为c
    lst = [list(map(int, input().strip().split(" "))) for _ in range(m)]
    # 按仇恨值c从大到小排序，优先处理高仇恨值的关系
    lst.sort(key=lambda x: x[2], reverse=True)
    ans = 0  # 初始化答案，默认无冲突时为0
    # 遍历排序后的关系
    for a, b, c in lst:
        # 若a和b在同一集合中，说明存在冲突（无法同时满足之前的关系）
        # 当前c是第一个冲突的最大仇恨值，即为答案
        if find_father(a) == find_father(b):
            ans = c
            break
        else:
            # 合并a与b的对立集合（a和b不能在同一集合，故a属于b的对立阵营）
            unite(a, b + n)
            # 合并b与a的对立集合（对称操作，确保关系一致性）
            unite(b, a + n)
    # 输出最大冲突仇恨值
    print(ans)
