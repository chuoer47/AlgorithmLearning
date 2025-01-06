from typing import List


class TARJAN:
    def __init__(self, n: int, g: List[List[int]]):
        # 记录结点的当前时间戳和最早时间戳,从根开始的一条路径上dfn 严格递增，low 严格非降
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.bridge = []  # 桥
        self.flag = [False] * n  # 是否是割点
        self.g = g

    def tarjan(self, o: int, f: int, t: int) -> None:
        self.dfn[o] = t
        self.low[o] = t
        c = 0
        for child in self.g[o]:
            if child != f:
                if self.dfn[child] == -1:
                    c += 1
                    self.tarjan(child, o, t + 1)
                    self.low[o] = min(self.low[o], self.low[child])
                    # 找到割点, 非root,有儿子
                    if self.dfn[o] <= self.low[child] and f != -1 and not self.flag[o]:
                        self.flag[o] = True
                    # 找到桥
                    if self.dfn[o] < self.low[child]:
                        self.bridge.append([o, child])
                else:
                    self.low[o] = min(self.low[o], self.dfn[child])
        # root点 儿子数大于等于2
        if f == -1 and c >= 2 and not self.flag[o]:
            self.flag[o] = True


class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        # 建图，跑tarjan
        # 主要是为了找【割点】
        n = len(cost)
        g = [[] for _ in range(n)]
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)
        # 题解|tarjan模板
        template = TARJAN(n, g)
        template.tarjan(0, -1, 0)

        ans = []
        vis = [0] * n
        for i in range(n):
            if template.flag[i] or vis[i]:
                # 如果是割点/已访问 跳过
                continue
            # BFS找当前连通支的最小花费
            res = cost[i]
            cur = [i]
            cv = set()
            while cur:
                x = cur.pop()
                vis[x] = 1
                for y in g[x]:
                    # 找连通支的割点
                    if template.flag[y]:
                        cv.add(y)
                    # 访问非割点cost
                    elif vis[y] == 0:
                        res = min(res, cost[y])
                        cur.append(y)
            if len(cv) < 2:
                # 如果有两个割点及以上
                # 说明该连通支绝对不能在初始的时候占据任意一个点
                # 不然会在后续的【夺回据点】导致图像的不连通
                # 因为只能一个一个点夺回，如果夺回到一个割点，【另一个割点会导致不连通】
                # 那为什么割点在1个及以下就可以？
                # 因为总能找到一个合法的推进顺序保证割点是最后一个夺取的
                ans.append(res)

        # 如果只有1个连通支，必须【夺取1个】，返回第1个
        # 不然，返回【前k-1个】的花销
        return ans[0] if len(ans) == 1 else sum(ans) - max(ans)
