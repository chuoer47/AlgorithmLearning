"""
小蓝有一棵树，树中包含 N 个结点，编号为 0, 1, 2, · · · , N − 1 ，其中每个
结点上都有一个整数 Xi 。他可以从树中任意选择两个不直接相连的结点 a 、b
并获得分数 Xa ⊕ Xb ，其中 ⊕ 表示按位异或操作。
请问小蓝可以获得的最大分数是多少？
"""
n = int(input())
node = list(map(int, input().split(" ")))
pivot = list(map(int, input().split(" ")))
res = 0
for i in range(n):
    for j in range(n):
        if i != j:  # 选择2个节点
            if pivot[j] != i and pivot[i] != j:  # 不相连
                res = max(res, node[i] ^ node[j])
print(res)
