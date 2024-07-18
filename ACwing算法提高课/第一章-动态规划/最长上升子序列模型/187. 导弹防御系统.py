"""
https://www.acwing.com/problem/content/189/

题解：
https://www.acwing.com/activity/content/code/content/1372317/
"""


def dfs(u, su, sd):
    """
    u:已经拦截的导弹数量(也可以理解为在拦截第u个导弹)
    su：上升的导弹数量
    sd：下降的导弹数量
    """
    global res
    if su + sd >= res:
        # 剪枝
        return
    if u == n:
        res = min(res, su + sd)
        return

    """第一种情况，加入到下降导弹拦截的队伍中"""
    k = 0
    while k < sd and down[k] <= weight[u]:
        k += 1
    t = down[k]
    down[k] = weight[u]
    if k < sd:
        dfs(u + 1, su, sd)
    else:
        dfs(u + 1, su, sd + 1)
    down[k] = t

    """第二种情况，加入到上升导弹拦截的队伍中"""
    k = 0
    while k < su and up[k] >= weight[u]:
        k += 1
    t = up[k]
    up[k] = weight[u]
    if k < su:
        dfs(u + 1, su, sd)
    else:
        dfs(u + 1, su + 1, sd)
    up[k] = t


N = 51
while True:
    n = int(input())
    if not n:
        break
    weight = list(map(int, input().strip().split(" ")))
    up = [0] * N
    down = [0] * N
    res = n
    dfs(0, 0, 0)
    print(res)
