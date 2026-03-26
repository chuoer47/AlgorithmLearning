"""
https://www.acwing.com/problem/content/description/1415/
"""
from collections import deque


def solve(lst: list):
    stack = [0]  # 单调栈
    area = 0  # 最大面积
    for i in range(1, c + 2):
        while stack and lst[stack[-1]] > lst[i]:
            x = stack.pop()
            if lst[x]: # 不等于0
                area = max(area, lst[x] * (i - stack[-1] - 1))
        stack.append(i)
    return area


r, c, p = map(int, input().split(" "))
set_in = set()
for _ in range(p):
    x, y = map(int, input().split(" "))
    set_in.add((x, y))
lst = [[0] * (c + 10) for _ in range(r + 10)]
# 初始化 O(n^2)
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if (i, j) in set_in:
            lst[i][j] = 0
        else:
            lst[i][j] = lst[i - 1][j] + 1
# 求解
res = 0
# 遍历每行
for i in range(1, r + 1):
    # print(lst[i])
    # print(solve(lst[i]))
    res = max(res, solve(lst[i]))
print(res)
