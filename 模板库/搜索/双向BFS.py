from collections import deque


def func1(num):
    # 这里写正向拓展
    return [num - 1, 2 * num]


def func2(num):
    # 这里写反向拓展
    if num % 2 == 0:
        return [num // 2, num + 1]
    return [num + 1]


def bidirectional_bfs(start, end):
    """
    双向BFS模板，用于寻找start到end的最短路径长度
    :param start: 起点
    :param end: 终点
    :param get_neighbors: 函数，输入当前节点，返回所有可达的邻居节点
    :return: 最短路径长度，若不可达返回-1
    """
    if start == end:
        return 0  # 起点终点相同的情况

    # 初始化两个方向的队列和已访问字典（记录节点到起点/终点的距离）
    queue_start = deque([start])
    visited_start = {start: 0}
    queue_end = deque([end])
    visited_end = {end: 0}
    get_neighbors = None
    flag = None

    while queue_start and queue_end:
        # 每次选择较小的队列进行处理，优化搜索效率
        if len(queue_start) <= len(queue_end):
            flag = True
            get_neighbors = func1
        else:
            flag = False
            get_neighbors = func2

        if flag:
            # 处理当前层的所有节点
            for _ in range(len(queue_start)):
                current = queue_start.popleft()

                # 遍历所有邻居节点
                for neighbor in get_neighbors(current):
                    if neighbor in visited_start:
                        continue  # 已访问过

                    # 如果该节点在另一方向已被访问，相遇条件达成
                    if neighbor in visited_end:
                        return visited_start[current] + 1 + visited_end[neighbor]

                    # 记录距离并加入队列
                    visited_start[neighbor] = visited_start[current] + 1
                    queue_start.append(neighbor)
        else:
            # 处理当前层的所有节点
            for _ in range(len(queue_end)):
                current = queue_end.popleft()

                # 遍历所有邻居节点
                for neighbor in get_neighbors(current):
                    if neighbor in visited_end:
                        continue  # 已访问过

                    # 如果该节点在另一方向已被访问，相遇条件达成
                    if neighbor in visited_start:
                        return visited_end[current] + 1 + visited_start[neighbor]

                    # 记录距离并加入队列
                    visited_end[neighbor] = visited_end[current] + 1
                    queue_end.append(neighbor)

    return -1  # 没有连通路径
