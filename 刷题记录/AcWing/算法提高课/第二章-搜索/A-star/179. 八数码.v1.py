"""
https://www.acwing.com/problem/content/181/

一开始考虑的是
https://oi-wiki.org/search/astar/
h 函数可以定义为，不在应该在的位置的数字个数。

函数性质不好，加上实现复杂，很容易爆了
"""
from copy import deepcopy


def inData2matrix(matrix, s):
    # 直接暴力录入了
    matrix[1][1] = s[0]
    matrix[1][2] = s[1]
    matrix[1][3] = s[2]
    matrix[2][1] = s[3]
    matrix[2][2] = s[4]
    matrix[2][3] = s[5]
    matrix[3][1] = s[6]
    matrix[3][2] = s[7]
    matrix[3][3] = s[8]


# 正确答案
template = [["#"] * 4 for _ in range(4)]
inData2matrix(template, "12345678x")


def calHx(matrix):
    """计算hx的值，返回不一样的函数"""
    ans = 0
    for i in range(1, 4):
        for j in range(1, 4):
            if matrix[i][j] != template[i][j]:
                ans += 1
    return ans


def findx(matrix):
    for i in range(1, 4):
        for j in range(1, 4):
            if matrix[i][j] == "x":
                return i, j


# 方向选择
chooses = {
    "u": [-1, 0],
    "d": [1, 0],
    "l": [0, -1],
    "r": [0, 1]
}

from heapq import *


def Astar():
    stack = [
        (calHx(matrix) + 0, 0, matrix, "")
    ]  # 第一项是hx+gx，第二项是gx, 第三项为当前矩阵，第四项是到达当前方案的步骤记录
    has = set()
    while stack:
        cost, gx, now, method = heappop(stack)
        if cost - gx == 0:
            return method
        has.add(str(now))
        x, y = findx(now)
        for choose in chooses:
            dx, dy = chooses[choose]
            if 1 <= x + dx <= 3 and 1 <= y + dy <= 3:
                next = deepcopy(now)
                next[x][y], next[x + dx][y + dy] = next[x + dx][y + dy], next[x][y]
                if str(next) not in has:
                    heappush(stack,
                             (calHx(next) + gx + 1, gx + 1, next, method + choose)
                             )


if __name__ == '__main__':
    s = input().strip().split(" ")
    matrix = [["#"] * 4 for _ in range(4)]
    inData2matrix(matrix, s)
    ans = Astar()
    print(ans)
