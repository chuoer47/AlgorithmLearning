"""
https://www.acwing.com/problem/content/3308/
"""

n, m, k, t = map(int, input().strip().split(" "))
time = [0] + list(map(int, input().strip().split(" ")))  # 获取种植时间
has = set(map(int, input().strip().split(" ")))  # 获取有的种子类型
# 初始化cost数组
cost = [float('inf') for _ in range(n + 10)]
for i in has:
    cost[i] = 0
way = [set() for _ in range(n + 10)]
for _ in range(k):
    a, b, c = map(int, input().strip().split(" "))
    way[c].add((a, b))

# 因为我想不明白终止条件，只能使用这样的实现方式，不过，效果还行，AC了
# 后面看了看题解，应该是测评数据量不够大，我没有用Dij都AC了
# 正确的解法应该考虑用最小堆，每次有最小的cost[i]，就放进去，然后去更新权重，我这样的写法算是取巧hhh
# 不过话又说回来，该算法时间复杂度确实高了点，但是算法还是正确的！
pre = cost.copy()
while True:
    for i in range(1, n + 1):
        if cost[i]:
            for a, b in way[i]:
                cost[i] = min(cost[i], max(cost[a], cost[b]) + max(time[a], time[b]))
    if cost == pre:
        break
    else:
        pre = cost.copy()
print(cost[t])
