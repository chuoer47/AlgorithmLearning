"""
基于斐波那契堆（Fibonacci Heap）优化的Prim算法

算法特性：
- 时间复杂度：O(E + V log V)，其中E为边数，V为顶点数
- 核心优化：利用斐波那契堆的高效decrease-key操作（摊还O(1)）
- 适用场景：大规模稀疏图的最小生成树求解

图的表示：邻接表（adjacency list）
- adj为列表，adj[u]存储与顶点u相连的边
- 每条边表示为元组 (v, weight)，即u与v之间的边权重为weight
"""


class FibonacciHeapNode:
    """斐波那契堆的节点结构"""

    def __init__(self, key, value):
        self.key = key  # 节点的键值（用于排序，对应边权重）
        self.value = value  # 节点存储的值（对应顶点编号）
        self.parent = None  # 父节点
        self.child = None  # 子节点（任意一个子节点）
        self.left = self  # 左兄弟（循环双链表）
        self.right = self  # 右兄弟（循环双链表）
        self.degree = 0  # 子节点数量
        self.mark = False  # 是否被标记（用于级联剪切）

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value})"


class FibonacciHeap:
    """斐波那契堆实现，支持Prim算法所需的核心操作"""

    def __init__(self):
        self.min_node = None  # 指向最小键值的节点
        self.nodes = {}  # 存储顶点值到节点的映射（用于快速查找）
        self.size = 0  # 堆中节点总数

    def insert(self, key, value):
        """插入新节点（键值为key，值为value）"""
        new_node = FibonacciHeapNode(key, value)
        self.nodes[value] = new_node  # 记录值到节点的映射
        self._merge_with_root_list(new_node)  # 合并到根链表

        # 更新最小节点
        if self.min_node is None or new_node.key < self.min_node.key:
            self.min_node = new_node

        self.size += 1
        return new_node

    def extract_min(self):
        """提取并返回最小键值的节点"""
        z = self.min_node
        if z is None:
            return None  # 堆为空

        # 将z的所有子节点添加到根链表
        if z.child is not None:
            child = z.child
            while True:
                next_child = child.right
                self._merge_with_root_list(child)  # 合并子节点到根链表
                child.parent = None
                if next_child == z.child:
                    break
                child = next_child

        # 从根链表中移除z
        self._remove_from_root_list(z)

        # 如果z是最后一个节点
        if z == z.right:
            self.min_node = None
        else:
            self.min_node = z.right
            self._consolidate()  # 合并相同度数的树

        # 从映射中移除
        del self.nodes[z.value]
        self.size -= 1
        return z

    def decrease_key(self, value, new_key):
        """将值为value的节点键值减小为new_key（new_key必须小于当前键值）"""
        if value not in self.nodes:
            return False  # 节点不存在

        x = self.nodes[value]
        if new_key >= x.key:
            return False  # 新键值必须更小

        x.key = new_key
        y = x.parent

        # 如果父节点存在且键值大于新键值，需要剪切
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)

        # 更新最小节点
        if x.key < self.min_node.key:
            self.min_node = x

        return True

    def is_empty(self):
        """判断堆是否为空"""
        return self.size == 0

    # 辅助方法：合并节点到根链表
    def _merge_with_root_list(self, node):
        if self.min_node is None:
            self.min_node = node
        else:
            # 插入到min_node的右侧
            node.right = self.min_node.right
            node.left = self.min_node
            self.min_node.right.left = node
            self.min_node.right = node

    # 辅助方法：从根链表移除节点
    def _remove_from_root_list(self, node):
        left = node.left
        right = node.right
        left.right = right
        right.left = left

    # 辅助方法：剪切节点（将子节点移到根链表）
    def _cut(self, x, y):
        # 从y的子节点中移除x
        if y.child == x:
            y.child = x.right if x != x.right else None
        if y.child is not None:
            x.left.right = x.right
            x.right.left = x.left

        y.degree -= 1  # 减少y的度数
        self._merge_with_root_list(x)  # 将x加入根链表
        x.parent = None
        x.mark = False  # 清除标记

    # 辅助方法：级联剪切（递归处理标记节点）
    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True  # 第一次剪切，标记y
            else:
                self._cut(y, z)  # 再次剪切，递归处理
                self._cascading_cut(z)

    # 辅助方法：合并相同度数的树（consolidate）
    def _consolidate(self):
        # 度数表，存储不同度数的根节点
        degree_table = {}

        # 遍历根链表所有节点
        current = self.min_node
        nodes = []
        while True:
            nodes.append(current)
            current = current.right
            if current == self.min_node:
                break

        for node in nodes:
            d = node.degree
            while d in degree_table:
                other = degree_table[d]
                if node.key > other.key:
                    node, other = other, node  # 确保node是较小键值的节点

                # 将other作为node的子节点
                self._remove_from_root_list(other)
                other.parent = node

                # 加入node的子链表
                if node.child is None:
                    node.child = other
                    other.left = other
                    other.right = other
                else:
                    other.right = node.child.right
                    other.left = node.child
                    node.child.right.left = other
                    node.child.right = other

                node.degree += 1
                other.mark = False
                del degree_table[d]
                d += 1

            degree_table[d] = node

        # 重新构建根链表并更新最小节点
        self.min_node = None
        for node in degree_table.values():
            if self.min_node is None:
                self.min_node = node
                node.left = node
                node.right = node
            else:
                self._merge_with_root_list(node)


def prim_mst_fibonacci(adj, n):
    """
    使用斐波那契堆优化的Prim算法求最小生成树

    算法思路：
    1. 初始化斐波那契堆，存储顶点及其到MST的最小边权重
    2. 从顶点0开始，逐步扩展MST，每次选取权重最小的边
    3. 利用斐波那契堆的decrease-key操作高效更新相邻顶点的权重

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

    # 初始化：所有顶点到MST的最小权重为无穷大
    INF = float('inf')
    min_weight = [INF] * n
    min_weight[0] = 0  # 从顶点0开始

    # 记录每个顶点在MST中的父节点
    parent = [-1] * n
    in_mst = [False] * n  # 标记是否已加入MST

    # 初始化斐波那契堆
    fib_heap = FibonacciHeap()
    for v in range(n):
        fib_heap.insert(min_weight[v], v)

    total_weight = 0
    mst_edges = []
    count = 0  # 已加入MST的顶点数

    while not fib_heap.is_empty():
        # 提取权重最小的顶点
        min_node = fib_heap.extract_min()
        u = min_node.value
        w = min_node.key

        # 若顶点已在MST中或权重为无穷大（图不连通），跳过
        if in_mst[u] or w == INF:
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

        # 更新相邻顶点的权重
        for v, weight in adj[u]:
            if not in_mst[v] and weight < min_weight[v]:
                min_weight[v] = weight
                parent[v] = u
                # 使用斐波那契堆的decrease-key操作更新权重
                fib_heap.decrease_key(v, weight)

    # 检查图是否连通
    if count != n:
        return (-1, [])  # 图不连通，无MST
    return (total_weight, mst_edges)


# ------------------------------ 示例用法 ------------------------------
if __name__ == "__main__":
    # 示例图（顶点0-4，5个顶点）
    adj = [
        [(1, 2), (3, 6)],  # 0连接1(2)、3(6)
        [(0, 2), (2, 3), (3, 8), (4, 5)],  # 1连接0(2)、2(3)、3(8)、4(5)
        [(1, 3), (4, 7)],  # 2连接1(3)、4(7)
        [(0, 6), (1, 8)],  # 3连接0(6)、1(8)
        [(1, 5), (2, 7)]  # 4连接1(5)、2(7)
    ]
    n = 5  # 顶点数

    # 测试斐波那契堆优化的Prim算法
    mst_weight, mst_edges = prim_mst_fibonacci(adj, n)
    print("斐波那契堆优化的Prim算法结果：")
    if mst_weight == -1:
        print("图不连通，无最小生成树")
    else:
        print(f"最小生成树总权重：{mst_weight}")
        print("包含的边：", mst_edges)
