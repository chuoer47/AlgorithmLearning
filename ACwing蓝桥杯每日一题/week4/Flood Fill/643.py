"""
https://www.acwing.com/problem/content/645/
朴素写法，每次都要进行判断，所以超时了
"""

import queue

options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
flag = []


def bfs(x, y):
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        i, j = q.get()
        for l, r in options:
            ii, jj = i + l, j + r
            if ii < 0 or ii >= R or jj < 0 or jj >= C:  # 越界
                continue
            else:
                if lst[ii][jj] == 1 and flag[ii][jj] == 0:
                    flag[ii][jj] = 1
                    q.put((ii, jj))


def solve():
    global flag
    flag = [[0] * C for _ in range(R)]
    res = 0
    for i in range(R):
        for j in range(C):
            if lst[i][j] == 1 and flag[i][j] == 0:
                res += 1
                bfs(i, j)
    return res


T = int(input())
for case in range(T):
    R, C = map(int, input().split(" "))
    output = []  # 输出队列
    t = [input() for _ in range(R)]
    lst = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if t[i][j] == "1":
                lst[i][j] = 1
    N = int(input())
    operate = [list(input().split(" ")) for _ in range(N)]
    for op in operate:
        if op[0] == "Q":
            res = solve()  # 广搜
            last = res
            output.append(res)
        else:
            x, y, z = map(int, op[1:])
            lst[x][y] = z
    print("Case #{}:".format(case + 1))
    for out in output:
        print(out)
