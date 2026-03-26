"""
https://www.acwing.com/problem/content/380/
"""
from sys import setrecursionlimit

setrecursionlimit(100000)

choose = [[-2, -1], [-2, 1], [-1, 2], [1, 2],
          [2, 1], [2, -1], [1, -2], [-1, -2]]  # 日字走法有八个选择
hasMatch = dict()
visit = set()


def find(x, y):
    """匈牙利匹配算法，使用深搜完成"""
    for dx, dy in choose:
        nx, ny = x + dx, y + dy  # nx,ny 相当于要匹配的奇数点
        if 1 <= nx <= n and 1 <= ny <= m:  # 在棋盘里面
            if (nx, ny) not in forbid and (nx, ny) not in visit:  # 可行且未被访问
                visit.add((nx, ny))
                if (nx, ny) not in hasMatch:  # 不在的话直接匹配
                    hasMatch[(nx, ny)] = (x, y)
                    return True
                else:
                    tx, ty = hasMatch[(nx, ny)]  # 在的话看看有没有机会找到一条拓广路
                    if find(tx, ty):  # 找拓广路，找到的话匹配成功
                        hasMatch[(nx, ny)] = (x, y)
                        return True
    return False


if __name__ == '__main__':
    n, m, t = map(int, input().strip().split(" "))
    forbid = set()  # 记录forbid为不准摆放的名单
    for _ in range(t):
        x, y = map(int, input().strip().split(" "))
        forbid.add((x, y))
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i + j) % 2 == 0 and (i, j) not in forbid:  # 可以放置
                visit = set()
                if find(i, j):  # 找一下能不能匹配到这个点
                    ans += 1
    print(n * m - t - ans)
