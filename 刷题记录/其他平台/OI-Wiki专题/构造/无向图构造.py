"""
给定一个整数 N，试构造一个节点数为 N 无向图。令节点编号为 1... N，要求其满足以下条件：
- 这是一个简单连通图。
- 存在一个整数 S 使得对于任意节点，与其相邻节点的下标和为 S。
保证输入数据有解。
"""

n = int(input())
graph = [[1 for _ in range(n + 1)] for i in range(n + 1)]  # n*n联通矩阵，下标从1开始


def solve(n, graph):
    if n < 3:
        return False
    if n % 2:
        for i in range(1, (n - 1) // 2 + 1):
            graph[i][n - i] = 0
            graph[n-i][i] = 0
    else:
        for i in range(1, n // 2 + 1):
            graph[i][n - i+1] = 0
            graph[n - i+1][i] = 0
    return True


solve(n, graph)
print(graph)
