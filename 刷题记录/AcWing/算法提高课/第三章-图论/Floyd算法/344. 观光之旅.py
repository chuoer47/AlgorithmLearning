"""
https://www.acwing.com/problem/content/346/
"""
N = 101
weight = [[float("inf")] * N for _ in range(N)]  # 记录权重
dis = [[float("inf")] * N for _ in range(N)]  # 记录距离矩阵
pos = [[0] * N for _ in range(N)]  # 记录中间点位置
path = []


def add(path, i, j):
    """Floyd算法的回溯查找路径"""
    mid = pos[i][j]
    if mid == 0:
        return
    add(path, i, mid)
    path.append(mid)
    add(path, mid, j)


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    for _ in range(m):
        u, v, l = map(int, input().strip().split(" "))
        weight[u][v] = weight[v][u] = min(weight[u][v], l)
        dis[u][v] = dis[v][u] = min(dis[u][v], l)
    for i in range(1, n + 1):
        weight[i][i] = 0
        dis[i][i] = 0

    ans = float("inf")
    for k in range(1, n + 1):
        """
        一定要先找环更新，再去更新距离矩阵
        这里算法的正确性的必要条件
        """
        # 第一步：看看有没有三个点以上的环
        # 这里i,j,k要满足互不相等的原则
        # 这里由于无向图的对称性，可以这么写
        for i in range(1, k + 1):
            for j in range(i + 1, k):
                if weight[i][k] + weight[k][j] + dis[i][j] < ans:
                    ans = weight[i][k] + weight[k][j] + dis[i][j]
                    # 记录路径
                    path = [k, i]
                    add(path, i, j)
                    path.append(j)

        # 第二步：更新距离矩阵，记得存中间结点
        # 这里就相当于在存矩阵
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    pos[i][j] = k

    if ans != float("inf"):
        print(*path)
    else:
        print("No solution.")
    print(ans)
