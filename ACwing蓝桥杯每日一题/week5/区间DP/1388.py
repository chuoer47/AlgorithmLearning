"""
https://www.acwing.com/problem/content/description/1390/
"""

# 录入数据
n = int(input())
lst = list(map(int, input().strip().split()))
while len(lst) < n:
    lst.extend(list(map(int, input().strip().split())))
# 初始化
dp = [[0] * (n + 10) for _ in range(n + 10)]
for length in range(1, n + 1):
    for i in range(n):
        if i + length - 1 < n:
            j = i + length - 1
            dp[i][j] = max(lst[i] - dp[i + 1][j],
                           lst[j] - dp[i][j - 1])
d = dp[0][n - 1]
# print(dp)
s = sum(lst)
print("{} {}".format((s + d) // 2, (s - d) // 2))
