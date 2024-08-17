"""
https://www.acwing.com/problem/content/1194/
"""


def topsort():
    """拓扑排序"""
    from collections import deque
    q = deque()
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            q.append((i, 0))
    # 这题目需要对队列进行一些小操作
    while q:
        now, price = q.popleft()
        ans.append(price)  # 录入价格
        for fa in graph[now]:
            in_deg[fa] -= 1
            if in_deg[fa] == 0:
                q.append((fa, price + 1))


if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    # 建图
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = []
    in_deg = [0] * (n + 1)
    # 录入数据
    for _ in range(m):
        a, b = map(int, input().strip().split(" "))
        graph[b].append(a)
        in_deg[a] += 1
    # 拓扑排序
    ans = []
    topsort()
    if len(ans) != n:
        print("Poor Xed")
    else:
        print(sum(ans) + 100 * n)
