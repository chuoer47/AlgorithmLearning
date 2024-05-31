"""
https://loj.ac/p/130
单点修改，区间查询
"""


def lowbit(x: int):
    return x & -x


def getsum(x):
    ans = 0
    while x > 0:
        ans += c[x]
        x -= lowbit(x)
    return ans


def add(pivot, v):
    while pivot <= n:
        c[pivot] += v
        pivot += lowbit(pivot)


if __name__ == '__main__':
    n, q = map(int, input().strip().split(" "))
    lst = [0] + list(map(int, input().strip().split(" ")))  # 方便下标操作
    ops = [list(map(int, input().strip().split(" "))) for _ in range(q)]
    c = [0] * (n + 10)  # 建立
    # O(n)版本，利用前缀和
    for i in range(1, n + 1):
        c[i] = lst[i] - lst[i - lowbit(i)]
    for i in range(n,0,-1):
        lst[i] = lst[i] - lst[i - 1]
    res = []
    # 建树
    # O(nlogn)版本
    # for i in range(1, n + 1):
    #     add(i, lst[i])
    for op in ops:
        type, t = op[0], op[1:]
        if type == 1:
            x, y, z = t
            add(x, z)
            add(y + 1, -z)
        else:
            t = t[0]
            print(getsum(t))