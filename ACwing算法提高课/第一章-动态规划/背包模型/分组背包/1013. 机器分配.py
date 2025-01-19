"""
https://www.acwing.com/problem/content/description/1015/

dp[i][j] i表示为选择前i个机器 j表示最大体积 属性最大价值

dp[i][j] = max{  dp[i-1][j-k] +  weight[i][k]  } k = 0,1,第 433 场周赛,...,j
"""

n, m = map(int, input().split(" "))
# 预处理价值矩阵
weight = [[0] * (m + 10) for i in range(n + 10)]
lst = [list(map(int, input().split(" "))) for _ in range(n)]
for i in range(n):
    for j in range(m):
        weight[i + 1][j + 1] = lst[i][j]
# DP
dp = [[0] * (m + 10) for i in range(n + 10)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(0, j + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + weight[i][k])
print(dp[n][m])
# 从后往前找路径
"""第一种方法，利用价值求解"""
# max_weight = dp[n][m]
# way = [0] * (n + 10)
# for i in range(n, 0, -1):
#     for j in range(1, m + 1):
#         for k in range(0, j + 1):
#             if dp[i - 1][j - k] + weight[i][k] == max_weight:
#                 way[i] = k
#                 max_weight -= weight[i][k]
#                 break
#         if way[i] != 0:
#             break

"""第二种方法，利用体积 只有这样才能过，很奇怪，题目说任意满足要求的都可以..."""
V = m
way = [0] * (n + 10)
for i in range(n, 0, -1):
    j = V
    for k in range(0, j + 1):
        if dp[i - 1][j - k] + weight[i][k] == dp[i][j]:
            way[i] = k
            V -= k
            break

# 输出
for i in range(1, n + 1):
    print("{} {}".format(i, way[i]))
