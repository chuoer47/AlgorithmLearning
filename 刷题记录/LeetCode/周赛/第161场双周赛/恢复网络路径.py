from cmath import inf
from collections import deque, defaultdict
from typing import List

min1 = lambda x, y: x if x < y else y
max1 = lambda x, y: x if x > y else y


def is_connect(g, n):
    q = deque([0])
    vis = set()
    while q:
        node = q.popleft()
        if node == n - 1:
            return True
        if node in vis:
            continue
        vis.add(node)
        for nxt, _ in g[node]:
            if nxt not in vis:
                q.append(nxt)
    return False


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        mx = 0
        for x, y, w in edges:
            if online[x] and online[y]:
                mx = max1(mx, w)
                g[x].append([y, w])
        if not is_connect(g, n):
            return -1

        def check(mid):
            # 返回最小边成本 >= mid
            # 有向无环，On能检查完毕
            def dfs(node, cost, min_cost):
                if cost > k or min_cost >= mid:
                    return False
                if node == n - 1:
                    return cost <= k and min_cost >= mid
                for nxt, w in g[node]:
                    if dfs(nxt, cost + w, min1(min_cost, w)):
                        return True
                return False

            return dfs(0, 0, inf)

        l, r = 0, mx
        ans = -1
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans

