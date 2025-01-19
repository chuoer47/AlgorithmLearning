"""
https://www.acwing.com/problem/content/2062/
题目思路：
1. 先通过深搜将两个斑点找到
第 433 场周赛. 在通过找到的两类，进行dfs。在dfs的过程中剪枝
"""
from math import inf
import sys

sys.setrecursionlimit(100000)  # 例如这里设置为十万

choose = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 方向选择
dis = inf


def judgeEdge(x, y):
    # 判断是否超出边界
    return x < 1 or x > n or y < 1 or y > m


def find(x, y):
    if judgeEdge(x, y) or (x, y) not in first:
        return
    first.remove((x, y))  # 移除
    second.append((x, y))  # 移入
    for l, r in choose:
        xx, yy = x + l, y + r
        if lst[xx][yy]:
            find(xx, yy)


def distance(x, y, ndis):
    """
    DFS广搜，找到最近的距离
    """
    dis = inf
    deque = [(x, y, ndis)]
    visit = [[0] * (m + 10) for i in range(n + 10)]
    visit[x][y] = 1
    while deque:
        x, y, ndis = deque.pop(0)
        if judgeEdge(x, y):
            continue
        for l, r in choose:
            xx, yy = x + l, y + r
            if lst[xx][yy]:  # 识别到1
                if (xx, yy) in second:  # 达到最近的第二类
                    dis = ndis
                    deque = []  # 清空列表
                    break
            else:
                if not visit[xx][yy]:  # 还有路走
                    visit[xx][yy] = 1
                    deque.append((xx, yy, ndis + 1))
    return dis


n, m = map(int, input().split(" "))
lst = [[0] * (m + 10) for i in range(n + 10)]
s = []
for i in range(n):
    s.append(input().strip())
first = []
second = []
# 获得矩阵
for i in range(n):
    ss = s[i]
    for ii in range(m):
        if ss[ii] == 'X':
            lst[i + 1][ii + 1] = 1
            first.append((i + 1, ii + 1))  # 保存斑点位置

x, y = first[0]
# find为找到两个斑点，然后再开始广搜
find(x, y)

dis = m * n
for x, y in first:
    dis = min(dis, distance(x, y, 0))
print(dis)
