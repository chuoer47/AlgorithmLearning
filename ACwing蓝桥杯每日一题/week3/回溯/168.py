"""
https://www.acwing.com/problem/content/170/
不会剪枝，数学不好，看不懂题解的剪枝方法....
"""
import math
from math import inf
import sys

sys.setrecursionlimit(100000)


def dfs(height, R, H):  # R,H表示为上一层的半径和高度
    """

    :param height: 第几层
    :param R: 半径
    :param H: 高度
    :return:
    """
    global area, t_area, n
    if height == m and n == 0:  # 完全搭建好
        area = min(area, t_area)
        print(t_area)
        return True
    elif height >= m:
        return
    if area != inf and t_area > area:  # 剪枝，即存在解法的时候，超过面积就返回
        return False
    flag = False
    for r in range(R - 1, 0, -1):  # 从高往低开始叠蛋糕
        t = n // (r * r)  # 求最高能叠到的高度
        for h in range(t, 0, -1):
            n -= r * r * h  # 减去体积
            t_area += 2 * r * h  # 加上面积
            if dfs(height + 1, r, h):  # 递归
                print(height + 1, r, h)
                flag = True
            #  还原现场
            t_area -= 2 * r * h
            n += r * r * h
    return flag


n = int(input())  # 表示体积
m = int(input())  # 表示层数
area = inf
t_area = 0
for i in range(int(math.sqrt(n)), 0, -1):
    t_area = i * i
    f = dfs(0, i + 1, 0)
    # print(i, f)
if area == inf:
    print(0)
else:
    print(area)
