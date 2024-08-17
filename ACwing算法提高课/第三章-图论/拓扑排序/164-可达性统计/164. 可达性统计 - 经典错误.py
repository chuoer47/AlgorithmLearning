"""
https://www.acwing.com/problem/content/166/

第一次尝试：这种写法属于典型错误，重复计算了
"""


def topsort():
    """拓扑排序"""
    from collections import deque
    q = deque()
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            q.append(i)
    # 这题目需要对队列进行一些小操作
    while q:
        now = q.popleft()
        for fa in graph[now]:
            in_deg[fa] -= 1
            ans[fa] += ans[now]
            if in_deg[fa] == 0:
                q.append(fa)


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    # 建图
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = set()
    in_deg = [0] * (n + 1)
    # 录入数据
    for _ in range(m):
        a, b = map(int, input().strip().split(" "))
        if a not in graph[b]:
            graph[b].add(a)
            in_deg[a] += 1
    print(in_deg)
    # 拓扑排序
    ans = [1] * (n + 1)
    topsort()
    for i in range(1, n + 1):
        print(ans[i])
