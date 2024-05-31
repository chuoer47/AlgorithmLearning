"""
https://www.acwing.com/problem/content/689/
"""
import queue
from math import inf

options = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def bfs(x, y):
    # print(x, y)
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        i, j = q.get()
        if st[i][j] > 0 or st[i][j] == -1:
            st[i][j] = -1
            continue
        st[i][j] = -1
        for l, r in options:
            ii, jj = i + l, j + r
            if ii < 0 or ii >= n or jj < 0 or jj >= n:
                continue
            else:
                if st[ii][jj] != -1:
                    q.put((ii, jj))
    # print(st)


cycle = int(input())
F = []
for _ in range(cycle):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    st = [[-1] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if lst[i][j] == "*":
                st[i][j] = -1
                continue
            if lst[i][j] == ".":
                mine = 0
                for l, r in options:
                    ii, jj = i + l, j + r
                    if ii < 0 or ii >= n or jj < 0 or jj >= n:
                        continue
                    else:
                        if lst[ii][jj] == "*":
                            mine += 1
                st[i][j] = mine
    res = 0
    for i in range(n):
        for j in range(n):
            if st[i][j] == 0:
                bfs(i, j)
                res += 1
    for i in range(n):
        for j in range(n):
            if st[i][j] != -1:
                res += 1
    F.append(res)
for p, i in enumerate(F):
    print("Case #{}: {}".format(p + 1, i))
