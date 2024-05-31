"""
https://www.acwing.com/file_system/file/content/whole/index/content/3940/
做不出来
"""
import sys

sys.setrecursionlimit(100000)


def dfs_node(node, father):
    """
    找到从node出发的价值最大的叶子节点和其路径
    :param node:
    :param father:
    :return:
    """
    if not dis[node]:
        return node, 0
    button_node, max_v, edge = node, 0, 0
    for next, value in dis[node]:
        if next != father:
            tem_node, tem_v = dfs_node(next, node)
            tem_v += value
            if tem_v > max_v:
                max_v = max(tem_v, max_v)
                button_node = tem_node
    return button_node, max_v


def dfs_num(node, father):
    """
    找到从node出发的价值最大的叶子节点和其路径
    :param node:
    :param father:
    :return:
    """
    global max_value
    if not dis[node]:
        return
    if max_value == 0:
        lst.append(seq.copy())  # 找到了一条序列
        return
    for next, value in dis[node]:
        if next != father:
            max_value -= value
            seq.append(next)
            dfs_num(next, node)
            seq.pop()
            max_value += value


n = int(input())
dis = [[] for i in range(n + 10)]
for i in range(n - 1):
    a, b, c = map(int, input().split(" "))
    dis[a].append((b, c))
    dis[b].append((a, c))
# print(dis)
first, first_value = dfs_node(1, -1)  # 找到直径的一端
second, max_value = dfs_node(first, -1)  # 找到直径的最大值
lst = []
seq = [first]
dfs_num(first, -1)
print(max_value)
print(lst)
