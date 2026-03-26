"""
https://www.acwing.com/problem/content/4410/
只用库函数的哈希还是会超时
"""
import sys

sys.setrecursionlimit(100000)


def judge(x, y, xx, yy, r):
    return (x - xx) ** 2 + (y - yy) ** 2 <= r ** 2


def dfs(x, y, r):
    global res
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if judge(x, y, i, j, r) and (i, j) in set_mine and (i, j) not in has_mine:
                has_mine.add((i, j))
                res += dict_num[(i, j)]
                dfs(i, j, dict_r[(i, j)])


n, m = map(int, input().strip().split(" "))
mines = [list(map(int, input().strip().split(" "))) for _ in range(n)]
fires = [list(map(int, input().strip().split(" "))) for _ in range(m)]
dict_num = dict()
set_mine = set()
dict_r = dict()
for mine in mines:
    x, y, r = mine
    # 处理dict_num
    if (x, y) not in dict_num:
        dict_num[(x, y)] = 1
    else:
        dict_num[(x, y)] += 1
    # 处理dict_r
    if (x, y) not in dict_r:
        dict_r[(x, y)] = r
    else:
        dict_r[(x, y)] = max(r, dict_r[(x, y)])
    # 处理set_mine
    set_mine.add((x, y))
has_mine = set()  # 已经处理过的地雷
res = 0  # 答案
for fire in fires:
    x, y, r = fire
    dfs(x, y, r)
print(res)
