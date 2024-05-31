"""
小蓝想制作一个吊坠，他手上有 n 个长度为 m 的首尾相连的环形字符串
{s1, s2, · · · , sn} ，他想用 n − 1 条边将这 n 个字符串连接起来做成吊坠，要求所
有的字符串连完后形成一个整体。连接两个字符串 si
, sj 的边的边权为这两个字
符串的最长公共子串的长度（可以按环形旋转改变起始位置，但不能翻转），小
蓝希望连完后的这 n − 1 条边的边权和最大，这样的吊坠他觉得最好看，请计算
最大的边权和是多少。
"""


def find(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find(parent, parent[vertex])


def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal_algorithm(graph):
    # 初始化结果
    minimum_spanning_tree = []

    # 初始化并查集
    parent = {vertex: vertex for vertex in graph.keys()}
    rank = {vertex: 0 for vertex in graph.keys()}

    # 获取所有的边
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((vertex, neighbor, weight))

    # 按权值排序边
    edges.sort(key=lambda edge: edge[2], reverse=True)  # 反转取最大的边

    # 不断取出权值最小的边并判断是否形成环
    for edge in edges:
        vertex1, vertex2, weight = edge
        if find(parent, vertex1) != find(parent, vertex2):
            union(parent, rank, vertex1, vertex2)
            minimum_spanning_tree.append(edge)

        if len(minimum_spanning_tree) == len(graph) - 1:
            break

    return minimum_spanning_tree


# 动态规划求解，存储解及解的计算过程
def lcs(x, y):  # 求解并存储箭头方向，x，y为字符串、列表等序列
    m = len(x)  # x的长度
    n = len(y)  # y的长度
    c = [[0 for i in range(n + 1)] for _ in range(m + 1)]  # 二维数组，初始值为0，用于存储长度结果
    d = [[0 for i in range(n + 1)] for _ in range(m + 1)]  # 二维数组，初始值为0，用于存储箭头方向,1表示左上，2表示上，3表示左
    for i in range(1, m + 1):  # 按行遍历二维数组
        for j in range(1, n + 1):  # 每行的各数值遍历， c0j和ci0相关的值都为0，所以均从1开始
            if x[i - 1] == y[j - 1]:  # xi=yi的情况，二维数组中i，j=0时，都为0已经确定，但字符串x，y仍需从0开始遍历
                c[i][j] = c[i - 1][j - 1] + 1  # 递推式
                d[i][j] = 1  # 箭头方向左上方
            elif c[i][j - 1] > c[i - 1][j]:  # 递推式，选择更大的
                c[i][j] = c[i][j - 1]
                d[i][j] = 3  # 箭头左边
            else:  # c[i-1][j] >= c[i][j-1]
                c[i][j] = c[i - 1][j]
                d[i][j] = 2  # 箭头上方
    return c[m][n], d


def longest_dis(i, j):
    a, b = lst[i], lst[j]
    res = 0
    for i in range(len(a)):
        t = a[i:] + a[:i]
        c, d = lcs(t, b)
        res = max(c, res)
    return res


# 求解距离矩阵
def distance():
    dis = dict()
    for i in range(1, n + 1):
        dis[lst[i]] = {}
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            tt = longest_dis(i, j)
            dis[lst[i]][lst[j]] = tt
            dis[lst[j]][lst[i]] = tt
    return dis


n,m = map(int,input().split())
lst = ["#"] + [input() for _ in range(n)]
dis = distance()  # 获得距离矩阵

p = kruskal_algorithm(dis)  # 求最大生成树
res = 0
for a, b, v in p:
    res += v
print(res)
