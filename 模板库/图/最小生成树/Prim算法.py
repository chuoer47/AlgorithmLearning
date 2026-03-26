"""
最小生成树（MST）算法模板（邻接表表示图）

包含两种经典算法：
1. Kruskal算法：基于边排序和并查集，适合稀疏图
2. Prim算法：基于顶点扩展和优先队列，适合稠密图

图的表示：邻接表（adjacency list）
- adj为列表，adj[u]存储与顶点u相连的边
- 每条边表示为元组 (v, weight)，即u与v之间的边权重为weight
"""

# ------------------------------ Prim算法 ------------------------------
import heapq


def prim_mst(adj, n):
    """
    使用Prim算法求最小生成树

    算法思路：
    1. 从任意顶点（默认0）开始，初始化优先队列
    2. 每次选取连接树内外的最短边，将新顶点加入树
    3. 重复直到所有顶点都加入树

    参数:
        adj: 邻接表，adj[u] = [(v, weight), ...]
        n: 顶点数量（顶点编号从0开始）

    返回:
        tuple: (mst_weight, mst_edges)
            - mst_weight: MST的总权重（若图不连通则返回-1）
            - mst_edges: MST包含的边列表，每条边为(u, v, weight)
    """
    if n == 0:
        return (0, [])

    # 标记顶点是否已加入MST
    in_mst = [False] * n
    # 存储每个顶点到MST的最小边权重（初始为无穷大）
    min_weight = [float('inf')] * n
    # 存储每个顶点在MST中的父节点
    parent = [-1] * n

    # 从顶点0开始，初始化其最小权重为0
    min_weight[0] = 0
    # 优先队列：(权重, 顶点)，用于选择下一条最短边
    heap = []
    heapq.heappush(heap, (0, 0))

    mst_edges = []
    total_weight = 0
    count = 0  # 已加入MST的顶点数

    while heap:
        w, u = heapq.heappop(heap)

        # 若顶点已在MST中，跳过
        if in_mst[u]:
            continue

        # 将顶点加入MST
        in_mst[u] = True
        total_weight += w
        count += 1

        # 记录边（除起点外）
        if parent[u] != -1:
            mst_edges.append((parent[u], u, w))

        # 若所有顶点都已加入，提前退出
        if count == n:
            break

        # 更新相邻顶点到MST的最小权重
        for v, weight in adj[u]:
            if not in_mst[v] and weight < min_weight[v]:
                min_weight[v] = weight
                parent[v] = u
                heapq.heappush(heap, (weight, v))

    # 检查图是否连通
    if count != n:
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

    # 测试Prim算法
    prim_weight, prim_edges = prim_mst(adj, n)
    print("\nPrim算法结果：")
    if prim_weight == -1:
        print("图不连通，无最小生成树")
    else:
        print(f"最小生成树总权重：{prim_weight}")
        print("包含的边：", prim_edges)
