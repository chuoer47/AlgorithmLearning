"""
https://www.acwing.com/problem/content/description/1129/

也超时了，md
"""
from collections import Counter


def Floyd(weight: list, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                weight[i][j] = min(weight[i][j], weight[i][k] + weight[k][j])


if __name__ == '__main__':
    n, p, c = map(int, input().strip().split(" "))
    weight = [[float("inf")] * (p + 10) for _ in range(p + 10)]
    cows = [int(input().strip()) for _ in range(n)]
    cnt = Counter(cows)
    for _ in range(c):
        rs, re, ci = map(int, input().strip().split(" "))
        weight[rs][re] = ci
        weight[re][rs] = ci
    for i in range(1, p + 1):
        weight[i][i] = 0
    # 使用Floyd计算最小距离
    Floyd(weight, p + 1)
    # 获取所有牛的距离矩阵
    dis = [0] * (p + 10)
    for cow, repeat in cnt.items():
        lst = weight[cow]
        for i in range(p + 10):
            dis[i] += lst[i] * repeat
    print(min(dis))
