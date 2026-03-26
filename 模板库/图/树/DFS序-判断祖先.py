from collections import defaultdict


class GraphAncestorAnalyzer:
    def __init__(self, nums, edges):
        self.nums = nums
        self.edges = edges
        self.n = len(nums)
        self.g = defaultdict(list)  # 图的邻接表表示
        self.v = [0] * self.n  # 存储每个节点的异或结果
        self._in = [0] * self.n  # 记录DFS进入时间
        self._out = [0] * self.n  # 记录DFS离开时间
        self.clock = 1  # 时间戳计数器

        # 初始化时构建图并执行DFS
        self.build_graph()
        self.dfs(0, -1)

    def build_graph(self):
        """构建图的邻接表"""
        for x, y in self.edges:
            self.g[x].append(y)
            self.g[y].append(x)

    def dfs(self, node, fa):
        """深度优先搜索，计算入时间、出时间和v值"""
        self.clock += 1
        self._in[node] = self.clock
        self.v[node] ^= self.nums[node]

        for ch in self.g[node]:
            if ch == fa:
                continue
            self.v[node] ^= self.dfs(ch, node)

        self._out[node] = self.clock
        return self.v[node]

    def is_ancestor(self, x, y):
        """判断x是否为y的祖先"""
        return self._in[x] < self._in[y] <= self._out[x]
