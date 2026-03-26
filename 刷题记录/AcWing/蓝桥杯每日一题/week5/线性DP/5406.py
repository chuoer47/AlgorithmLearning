"""
https://www.acwing.com/problem/content/5409/
"""

# 录入数据
s = input()
# 初始化w数组
w = [ord(i) - ord('a') + 1 for i in s]
n = len(s)
# 特判
if n <= 2:
    print(max(w))
    exit()
dp = [0] * n
dp[0], dp[1] = w[0], max(w[0], w[1])  # 这里一开始没想到，浪费了贼多时间
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + w[i])
print(dp[-1])
