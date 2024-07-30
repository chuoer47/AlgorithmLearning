"""
https://www.acwing.com/problem/content/248/
利用差分，直接套模板了
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
    c = [0] * (n + 10)  # 建立树状数组空间
    # 建树
    for i in range(1, n + 1):
        add(i, lst[i]-lst[i-1])
    del lst
    ops = [list(input().strip().split(" ")) for _ in range(q)]  # 一次性录入完毕
    for op in ops:
        if op[0] == "Q":
            print(getsum(int(op[1])))
        else:
            l, r, d = map(int, op[1:])
            add(l,d)
            add(r+1,-d)
