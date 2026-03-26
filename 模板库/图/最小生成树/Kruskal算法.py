"""
最小生成树（MST）算法模板（邻接表表示图）

包含两种经典算法：
1. Kruskal算法：基于边排序和并查集，适合稀疏图
2. Prim算法：基于顶点扩展和优先队列，适合稠密图

图的表示：邻接表（adjacency list）
- adj为列表，adj[u]存储与顶点u相连的边
- 每条边表示为元组 (v, weight)，即u与v之间的边权重为weight
"""


# ------------------------------ Kruskal算法 ------------------------------
class UnionFind:
    """并查集（Union-Find）数据结构，用于Kruskal算法检测环"""

    def __init__(self, size):
        self.parent = list(range(size))  # 父节点数组
        self.rank = [0] * size  # 用于路径压缩的秩数组

    def find(self, x):
        """查找x的根节点，带路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 递归压缩路径
        return self.parent[x]

    def union(self, x, y):
        """合并x和y所在的集合，带按秩合并"""
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False  # 已在同一集合，合并失败（存在环）

        # 按秩合并：将秩小的树合并到秩大的树
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return True  # 合并成功


def kruskal_mst(adj, n):
    """
    使用Kruskal算法求最小生成树

    算法思路：
    1. 将所有边按权重从小到大排序
    2. 依次选取边，通过并查集判断是否形成环
    3. 若不形成环则加入MST，直到选取n-1条边（n为顶点数）

    参数:
        adj: 邻接表，adj[u] = [(v, weight), ...]
        n: 顶点数量（顶点编号从0开始）

    返回:
        tuple: (mst_weight, mst_edges)
            - mst_weight: MST的总权重（若图不连通则返回-1）
            - mst_edges: MST包含的边列表，每条边为(u, v, weight)
    """
    # 1. 提取所有边并去重（避免重复处理u-v和v-u）
    edges = []
    for u in range(n):
        for v, w in adj[u]:
            if u < v:  # 只添加一次u-v（避免重复）
                edges.append((w, u, v))

    # 2. 按权重从小到大排序
    edges.sort()

    # 3. 初始化并查集和MST变量
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0

    # 4. 依次选取边
    for w, u, v in edges:
        if uf.union(u, v):  # 无环则加入MST
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == n - 1:  # 已找到n-1条边，MST完成
                break

    # 检查图是否连通（MST应包含n-1条边）
    if len(mst_edges) != n - 1:
        return (-1, [])  # 图不连通，无MST
    return (total_weight, mst_edges)


# ------------------------------ 示例用法 ------------------------------
if __name__ == "__main__":
    # 示例图（顶点0-4，5个顶点）
    # 邻接表表示：adj[u] = [(v, weight), ...]
    adj = [
        [(1, 2), (3, 6)],  # 0连接1(2)、3(6)
        [(0, 2), (2, 3), (3, 8), (4, 5)],  # 1连接0(2)、2(3)、3(8)、4(5)
        [(1, 3), (4, 7)],  # 2连接1(3)、4(7)
        [(0, 6), (1, 8)],  # 3连接0(6)、1(8)
        [(1, 5), (2, 7)]  # 4连接1(5)、2(7)
    ]
    n = 5  # 顶点数

    # 测试Kruskal算法
    kruskal_weight, kruskal_edges = kruskal_mst(adj, n)
    print("Kruskal算法结果：")
    if kruskal_weight == -1:
        print("图不连通，无最小生成树")
    else:
        print(f"最小生成树总权重：{kruskal_weight}")
        print("包含的边：", kruskal_edges)
