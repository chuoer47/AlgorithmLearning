"""
https://www.acwing.com/problem/content/1404/
"""
from math import sqrt

dict2char = dict()
c = 'a'
pivot = 0


def get_dis():  # 计算距离，作为哈希值
    res = 0
    for i in range(len(now_lst)):
        for j in range(i + 1, len(now_lst)):
            x, y = now_lst[i]
            xx, yy = now_lst[j]
            res += sqrt((x - xx) ** 2 + (y - yy) ** 2)
    return res


def get_char(dis):  # 得到字符
    global dict2char, c
    dis = int(dis * 10000)  # 取精度
    if dis not in dict2char:
        dict2char[dis] = c
        c = chr(ord(c) + 1)
    return dict2char[dis]


def dfs(x, y):  # 找出联通图
    if (x, y) not in now:
        now.add((x, y))
        now_lst.append((x, y))
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if i < 0 or i >= h or j < 0 or j >= w:
                continue
            if lst[i][j] == "1" and (i, j) not in now:
                now.add((i, j))
                now_lst.append((i, j))
                dfs(i, j)


# 数据处理
w = int(input())
h = int(input())
lst = [list(input()) for i in range(h)]
now = set()
now_lst = []
# 查找
for x in range(h):
    for y in range(w):
        if lst[x][y] == "1":
            now = set()
            now_lst = []
            # 递归
            dfs(x, y)
            dis = get_dis()
            cc = get_char(dis)
            while now:
                xx, yy = now.pop()
                lst[xx][yy] = cc
for x in range(h):
    print("".join(lst[x]))
