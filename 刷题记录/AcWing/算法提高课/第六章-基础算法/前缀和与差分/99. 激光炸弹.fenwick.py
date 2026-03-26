"""
https://www.acwing.com/problem/content/101/

居然没过，卡太严格了...
TLE 通过了 4/14个数据
就查询多了4个log的数量级都过不了
"""

# 树状数组模板
# 单点修改，区间查询
# 需要注意树状数组下标从1开始，需要预处理数据
N = 5010  # 需要时修改
tr = [[0] * N for _ in range(N)]


def lowbit(x):
    return x & -x


def add(x, y, k, tr, n=N, m=N):
    """在(x,y)坐标点添加k"""
    while x <= n:
        yy = y
        while yy <= m:
            tr[x][yy] += k
            yy += lowbit(yy)
        x += lowbit(x)


def getSum(x, y, tr):
    ans = 0
    while x:
        yy = y
        while yy:
            ans += tr[x][yy]
            yy -= lowbit(yy)
        x -= lowbit(x)
    return ans


def query(a, b, c, d, tr):
    """左上角为(a,b),右下角为(c,d)"""
    return getSum(c, d, tr) - getSum(a - 1, d, tr) - getSum(c, b - 1, tr) + getSum(a - 1, b - 1, tr)


if __name__ == '__main__':
    n, r = map(int, input().split(" "))
    r = min(r, 5001)  # 优化一下r
    if r == 0:
        """特判一下"""
        print(0)
        exit(1)
    # 数据录入
    row, col = 0, 0
    for _ in range(n):
        x, y, w = map(int, input().split(" "))
        row, col = max(row, x + 1), max(col, y + 1)
        add(x + 1, y + 1, w, tr)
    ans = 0
    # 需要对滑动窗口判断一下
    t = max(row, col)
    if r >= max(row, col):
        ans = max(ans, query(5002, 5002, 1, 1, tr))
    # 滑动窗口启动！ (i,j)表示为滑动窗口的左上角
    for i in range(1, t - r + 1):
        for j in range(1, t - r + 1):
            ans = max(ans, query(i, j, i + r - 1, j + r - 1, tr))
    print(ans)
