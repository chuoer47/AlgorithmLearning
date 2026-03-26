"""
Bron–Kerbosch算法模板（带pivot优化）

算法功能：寻找无向图中的所有最大团（max cliques）
最大团定义：图中顶点的子集，子集内任意两个顶点都相邻（完全子图），且无法再添加其他顶点保持这一性质

核心优势：通过递归回溯和pivot优化，高效枚举所有团并筛选最大团
时间复杂度：最坏情况下O(3^(n/3))（n为顶点数），pivot优化可显著减少实际运行时间
"""


def edges_to_adjacency(edges: list) -> dict:
    """将边列表转换为邻接表表示

    邻接表是图的一种高效存储方式，用于快速查询顶点的邻居

    参数:
        edges: 边列表，格式为edges[u] = [v1, v2, ...]，表示顶点u与v1, v2等相邻

    返回:
        dict: 邻接表，键为顶点，值为该顶点的所有邻居组成的集合
    """
    # 顶点数量为边列表的长度（假设顶点编号从0开始连续）
    n = len(edges)
    # 初始化邻接表：每个顶点对应一个空集合
    adj = {i: set() for i in range(n)}

    for u in range(n):
        # 遍历顶点u的所有邻居v
        for v in edges[u]:
            # 确保顶点索引有效（不超出范围）
            if v < n:
                # 无向图：u的邻居包含v，v的邻居也包含u
                adj[u].add(v)
                adj[v].add(u)

    return adj


def bron_kerbosch(R: set, P: set, X: set, adj: dict, cliques: list) -> None:
    """Bron–Kerbosch递归算法（带pivot优化），用于枚举图中所有团

    算法核心思想：
    - 维护三个集合：当前团R（正在构建的团）、候选顶点P（可加入R的顶点）、排除顶点X（不可加入R的顶点）
    - 当P和X都为空时，R是一个团，加入结果列表
    - 通过pivot优化减少递归分支：选择P∪X中的一个顶点作为pivot，只迭代P中不与pivot相邻的顶点

    参数:
        R: 当前正在构建的团（初始为空集）
        P: 候选顶点集（可能加入R的顶点，初始为所有顶点）
        X: 排除顶点集（不可加入R的顶点，初始为空集）
        adj: 图的邻接表
        cliques: 用于存储所有团的列表（结果会直接写入该列表）
    """
    # 终止条件：若候选集和排除集都为空，当前R是一个团
    if not P and not X:
        cliques.append(R.copy())  # 复制R并加入结果
        return

    # pivot优化：从P∪X中选一个顶点作为pivot，减少需要迭代的顶点
    # 若P∪X为空，直接使用None（此时P必为空，会触发终止条件）
    pivot = next(iter(P | X)) if (P | X) else None

    # 只迭代P中不与pivot相邻的顶点（若pivot存在），否则迭代所有P
    # 这一步是优化的核心，可大幅减少递归次数
    for v in P - adj.get(pivot, set()):
        # 递归：将v加入当前团R，更新候选集为P与v的邻居的交集（保证团的完全性）
        # 排除集更新为X与v的邻居的交集
        bron_kerbosch(
            R=R | {v},  # 当前团加入v
            P=P & adj[v],  # 新候选集：只能是v的邻居（确保与v相邻）
            X=X & adj[v],  # 新排除集：只能是v的邻居
            adj=adj,
            cliques=cliques
        )

        # 回溯：将v从候选集移到排除集（已考虑过包含v的情况，后续不再考虑）
        P.remove(v)
        X.add(v)


def find_max_cliques(edges: list) -> list:
    """寻找无向图中的所有最大团

    流程：
    1. 将边列表转换为邻接表
    2. 调用Bron–Kerbosch算法枚举所有团
    3. 筛选出其中尺寸最大的团

    参数:
        edges: 边列表，格式为edges[u] = [v1, v2, ...]，表示顶点u与v1, v2等相邻

    返回:
        list: 所有最大团的列表，每个团以顶点集合的形式存在
              若图中无团（仅可能为顶点数0的情况），返回空列表
    """
    # 转换为邻接表
    adj = edges_to_adjacency(edges)
    # 顶点数量
    n = len(adj)

    # 存储所有找到的团
    cliques = []

    # 初始调用：R为空，P为所有顶点，X为空
    bron_kerbosch(
        R=set(),
        P=set(range(n)),
        X=set(),
        adj=adj,
        cliques=cliques
    )

    # 若没有找到团，返回空列表
    if not cliques:
        return []

    # 找到最大团的尺寸
    max_size = max(len(clique) for clique in cliques)

    # 筛选出所有尺寸为最大的团
    return [clique for clique in cliques if len(clique) == max_size]


# 示例用法
if __name__ == "__main__":
    # 示例1：三角形（3个顶点彼此相邻，最大团是整个集合）
    edges1 = [
        [1, 2],  # 顶点0与1、2相邻
        [0, 2],  # 顶点1与0、2相邻
        [0, 1]  # 顶点2与0、1相邻
    ]
    print("示例1最大团：", find_max_cliques(edges1))  # 输出：[{0, 1, 2}]

    # 示例2：4顶点图（最大团为3个顶点）
    edges2 = [
        [1, 2, 3],  # 0与1、2、3相邻
        [0, 2],  # 1与0、2相邻
        [0, 1, 3],  # 2与0、1、3相邻
        [0, 2]  # 3与0、2相邻
    ]
    print("示例2最大团：", find_max_cliques(edges2))  # 输出：[{0, 2, 3}, {0, 1, 2}]

    # 示例3：独立顶点（无相邻边，最大团为单个顶点）
    edges3 = [[], [], []]  # 3个孤立顶点
    print("示例3最大团：", find_max_cliques(edges3))  # 输出：[{0}, {1}, {2}]
