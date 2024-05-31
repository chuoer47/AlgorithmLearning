"""
https://www.acwing.com/problem/content/1373/
"""

v, n = map(int, input().split())
money = []
# 录入数据
money.extend(list(map(int, input().split())))
while len(money) < v:
    money.extend(list(map(int, input().split())))
dp = [0] * (n + 10)
dp[0] = 1
# 每种钱只依靠dp[i-m]
for m in money:
    for i in range(m, n + 1):
        dp[i] += dp[i - m]
print(dp[n])
