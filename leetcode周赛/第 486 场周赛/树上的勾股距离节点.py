class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        # 想直接树上lca + 暴力遍历判断 => nlogn 能解决
        # 或者可以这样，维护三个dfs，每次找出所有点到根节点的距离
        # 更广泛的情况还可以用换根DP进行任意一个点到另一个点的距离的计算？（好像没有lca来的方便）

        g = [[] for _ in range(n)]
        d = [[0] * n for _ in range(3)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, fa, d, nums):
            nums[node] = d
            for nxt in g[node]:
                if nxt == fa:
                    continue
                dfs(nxt, node, d + 1, nums)

        dfs(x, -1, 0, d[0])
        dfs(y, -1, 0, d[1])
        dfs(z, -1, 0, d[2])

        ans = 0
        for a, b, c in zip(*d):
            a, b, c = sorted([a, b, c])
            if a * a + b * b == c * c:
                ans += 1
        return ans