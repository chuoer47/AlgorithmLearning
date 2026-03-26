"""
https://www.acwing.com/problem/content/3497/
"""


def count_one(x):
    cnt = 0
    while x:
        cnt += 1
        x -= x & -x
    return cnt


n, m, k = map(int, input().strip().split(" "))
MOD = int(1e9 + 7)
# 建立DP数组
f = [[[[0] * (k + 1)
       for _ in range(1 << n)]
      for _ in range(1 << n)]
     for _ in range(m + 3)]
f[0][0][0][0] = 1  # 初始化
cnt_pre = [count_one(i) for i in range(1 << n)]  # 预处理数组，加快速度

# 开始dp
for i in range(1, m + 3):
    for a in range(1 << n):
        for b in range(1 << n):
            if (a & (b << 2)) or (b & (a << 2)):  # 冲突了
                continue
            for c in range(1 << n):
                if (c & (a << 2)) or (a & (c << 2)) or (c & (b << 1)) or (b & (c << 1)):
                    continue
                cnt = cnt_pre[b]
                for j in range(cnt, k + 1):
                    f[i][a][b][j] = (f[i][a][b][j] + f[i - 1][c][a][j - cnt]) % MOD

# 完成DP，输出结果
print(f[m + 2][0][0][k])
