"""
https://www.acwing.com/problem/content/description/314/
"""


def cal_step(a, b, c, d):
    return a + 2 * b + 3 * c + 4 * d


# 数据录入
n, m = map(int, input().split(" "))
w = list(map(int, input().split(" ")))
step = list(map(int, input().split(" ")))
# 处理数据
num = [0] * 5
for s in step:
    num[s] += 1
# 创建dp数组
dp = [[[[0] * 41
        for _ in range(41)]
       for _ in range(41)]
      for _ in range(41)]
dp[0][0][0][0] = w[0] # 初始化
for a in range(num[1] + 1):
    for b in range(num[2] + 1):
        for c in range(num[3] + 1):
            for d in range(num[4] + 1):
                step = cal_step(a, b, c, d)
                if a:
                    dp[a][b][c][d] = max(dp[a][b][c][d], dp[a - 1][b][c][d] + w[step])
                if b:
                    dp[a][b][c][d] = max(dp[a][b][c][d], dp[a][b - 1][c][d] + w[step])
                if c:
                    dp[a][b][c][d] = max(dp[a][b][c][d], dp[a][b][c - 1][d] + w[step])
                if d:
                    # print(a,b,c,d,step)
                    dp[a][b][c][d] = max(dp[a][b][c][d], dp[a][b][c][d - 1] + w[step])

print(dp[num[1]][num[2]][num[3]][num[4]])
