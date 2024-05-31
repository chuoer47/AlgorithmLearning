"""
https://www.acwing.com/problem/content/4410/
看大佬题解，使用了队列简化降低了运行时间，笑死，python递归真不行啊
"""
import sys
from collections import Counter, deque

sys.setrecursionlimit(100000)


def judge(x, y, xx, yy, r):
    return (x - xx) ** 2 + (y - yy) ** 2 <= r ** 2


n, m = map(int, input().strip().split(" "))
mines = [list(map(int, input().strip().split(" "))) for _ in range(n)]
fires = [list(map(int, input().strip().split(" "))) for _ in range(m)]
dict_mine = dict()
has_mine = set()
# 地雷预处理
for mine in mines:
    x, y, r = mine
    # 处理dict
    if (x, y) not in dict_mine:
        dict_mine[(x, y)] = Counter()
    dict_mine[(x, y)][r] += 1

res = 0  # 答案
dict_fire = Counter()
# 处理一样的，和地雷半径最大的
for fire in fires:
    x, y, r = fire
    if r > dict_fire[(x, y)]:
        dict_fire[(x, y)] = r

q = deque()
# 处理
for (x, y), r in dict_fire.items():
    q.append((x, y, r))

while q:
    x, y, r = q.popleft()
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if judge(x, y, i, j, r) and (i, j) in dict_mine and (i,j) not in has_mine:
                res += sum(dict_mine[(i, j)].values())
                q.append((i, j, max(dict_mine[(i, j)].keys())))
                has_mine.add((i,j))
print(res)
