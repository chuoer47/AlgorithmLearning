"""
匈牙利算法模板（用于求解有向图最小路径覆盖问题）

问题背景：
在有向图中，最小路径覆盖是指用最少的路径覆盖所有顶点，且每个顶点仅被一条路径包含。
通过将问题转化为二分图最大匹配问题求解，公式为：最小路径数 = 顶点数 - 最大匹配数

算法流程：
1. 计算有向图的传递闭包（使间接可达变为直接可达）
2. 利用匈牙利算法求解二分图的最大匹配
3. 根据最大匹配结果计算最小路径覆盖

时间复杂度：
- 传递闭包计算：O(n³)（基于Floyd思想）
- 匈牙利算法：O(nm)（n为顶点数，m为边数）
"""


def hungarian_min_path_cover(n, edges):
    """
    求解有向图的最小路径覆盖

    参数:
        n: 顶点数量（顶点编号从1开始）
        edges: 边的列表，每个元素为(a, b)表示有向边a->b

    返回:
        int: 最小路径覆盖的路径数量
    """
    # 构建邻接矩阵表示有向图（传递闭包的初始状态）
    # link[i][j] = 1 表示存在路径i->j（初始为直接边）
    link = [[0] * (n + 1) for _ in range(n + 1)]
    for a, b in edges:
        link[a][b] = 1

    # 计算传递闭包（Floyd算法思想）
    # 若i可通过k到达j，则i直接可达j
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                link[i][j] |= link[i][k] & link[k][j]  # 逻辑或运算：若已有路径则保持1

    # 匈牙利算法相关变量
    match = [0] * (n + 1)  # 匹配数组：match[j] = i 表示右部节点j匹配左部节点i
    result = 0  # 最大匹配数

    def find(x, visited):
        """
        寻找增广路径（匈牙利算法核心）

        参数:
            x: 当前需要匹配的左部节点
            visited: 标记右部节点是否已访问（避免重复搜索）

        返回:
            bool: 是否找到增广路径
        """
        # 遍历所有可能的右部节点
        for j in range(1, n + 1):
            # 若x可到达j且j未被访问
            if link[x][j] and not visited[j]:
                visited[j] = True  # 标记为已访问
                # 若j未匹配，或j的匹配节点可找到其他路径
                if match[j] == 0 or find(match[j], visited):
                    match[j] = x  # 更新匹配关系
                    return True
        return False  # 未找到增广路径

    # 对每个左部节点尝试匹配
    for i in range(1, n + 1):
        visited = [False] * (n + 1)  # 每次匹配重置访问标记
        if find(i, visited):
            result += 1  # 找到匹配，增加最大匹配数

    # 最小路径数 = 顶点数 - 最大匹配数
    return n - result


# 示例用法
if __name__ == '__main__':
    # 读取输入（顶点数n，边数m）
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        edges.append((a, b))

    # 计算并输出最小路径覆盖
    print(hungarian_min_path_cover(n, edges))
