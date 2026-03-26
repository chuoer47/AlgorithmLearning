"""
https://www.acwing.com/problem/content/166/

二进制完成
TLE 通过了 4/5个数据
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
            ans[fa] = ans[fa] | ans[now]
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
    # 拓扑排序
    ans = [1 << i for i in range(n + 1)]
    topsort()
    for i in range(1, n + 1):
        print(bin(ans[i]).count("1"))