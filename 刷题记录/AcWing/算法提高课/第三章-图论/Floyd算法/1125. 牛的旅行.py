"""
https://www.acwing.com/problem/content/1127/
"""


def calDis(i, j):
    xi, yi = index[i]
    xj, yj = index[j]
    return ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5


if __name__ == '__main__':
    n = int(input())
    index = []
    area = []
    for _ in range(n):
        x, y = map(int, input().strip().split(" "))
        index.append([x, y])
    for _ in range(n):
        area.append(list(map(int, list(input().strip()))))

    # 算距离+初始化
    for i in range(n):
        for j in range(n):
            if area[i][j] == 1 or i == j:
                area[i][j] = calDis(i, j)
            else:
                area[i][j] = float("inf")

    # Floyd算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                area[i][j] = min(area[i][j], area[i][k] + area[k][j])

    # 把到达不到的距离设为-1,方便下面操作
    for i in range(n):
        for j in range(n):
            if area[i][j] == float("inf"):
                area[i][j] = -1

    # 计算每一点距离最大值
    maxP = [max(area[i]) for i in range(n)]
    ans = float("inf")

    # 计算答案
    for i in range(n):
        for j in range(n):
            if area[i][j] == -1:
                ans = min(ans, maxP[i] + calDis(i, j) + maxP[j])

    print("{:0.6f}".format(max(max(maxP), ans)))
