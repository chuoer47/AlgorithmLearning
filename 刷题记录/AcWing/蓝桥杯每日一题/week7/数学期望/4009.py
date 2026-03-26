"""
https://www.acwing.com/problem/content/4012/
我简单地算了一下，N=16,K=5,大概8千万运算量，会超时
目前没想到什么剪枝方法hhhh
"""


def countOne(x):
    ans = 0
    while x:
        ans += 1
        x -= (x & -x)
    return ans


n, K = map(int, input().split(" "))
p = list(map(float, input().split(" ")))
y = 1 << n
x = K * n + 1  # 这里x还需要定夺一下取值...
# 预处理数组，减少时间常数
cntLst = [0] * y
for i in range(y):
    cntLst[i] = countOne(i)
# DP
dp = [[[0] * 2  # 第一个表示概率，第二个表示是否满足集齐硬币的条件
       for _ in range(y)]
      for _ in range(x)]
dp[0][0][0] = 1
res = 0
for i in range(1, x):
    for j in range(y):
        for k in range(n):
            if j & (1 << k):
                if dp[i - 1][j][1] == 0:
                    dp[i][j][0] += dp[i - 1][j][0] * p[k]
                if dp[i - 1][j - (1 << k)][1] == 0:
                    dp[i][j][0] += dp[i - 1][j - (1 << k)][0] * p[k]
        cnt = cntLst[j]
        if ((i - cnt) // K) >= (n - cnt):
            res += dp[i][j][0] * i
            dp[i][j][1] = 1
print(res)
