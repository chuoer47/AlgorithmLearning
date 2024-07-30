"""
https://www.acwing.com/problem/content/97/
"""
from copy import deepcopy

choose = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]


def click(area, row, col):
    for dx, dy in choose:
        if 0 <= row + dx < 5 and 0 <= col + dy < 5:
            if area[row + dx][col + dy] == "1":
                area[row + dx][col + dy] = "0"
            else:
                area[row + dx][col + dy] = "1"


def trans(way, area, row=0):
    way = "0" * (5 - len(bin(way)[2:])) + bin(way)[2:]  # 必须要这么操作一下，比较方便表达
    for i, v in enumerate(way):
        if v == "1":  # 需要点击一下
            click(area, row, i)


def solve(lst: list):
    """解决单张地图的问题，area 为5*5的矩阵"""
    ans = 7
    for i in range(1 << 5):
        area = deepcopy(lst)  # 每次复制一下，懒得复原了
        step = bin(i).count("1")  # 记录点击次数
        trans(i, area)
        # 开始遍历后边4行了
        for j in range(1, 5):
            for k in range(5):
                if area[j - 1][k] == "0":
                    click(area, j, k)
                    step += 1
        # 判定是否满足条件
        if step <= 6 and sum(map(int, area[-1])) == 5:
            ans = min(ans, step)
    return ans if ans <= 6 else -1


if __name__ == '__main__':
    n = int(input())
    for turn in range(n):
        if turn > 0:
            input()  # 去除空行
        lst = [list(input().strip()) for _ in range(5)]
        print(solve(lst))
