"""
https://www.acwing.com/problem/content/4264/
"""

n = int(input())
s = "#" + input()
l, r = [0] * (n + 10), [0] * (n + 10)

# 从左往右开始计算
h, g = 0, 0
for i in range(1, n + 1):
    if s[i] == "G":
        l[i] = h
        h = 0
        g += 1
    else:
        l[i] = g
        g = 0
        h += 1

# 从右往左开始计算
h, g = 0, 0
for i in range(n, 0, -1):
    if s[i] == "G":
        r[i] = h
        h = 0
        g += 1
    else:
        r[i] = g
        g = 0
        h += 1

# 枚举遍历
res = 0
for i in range(1, n + 1):
    res += l[i] * r[i] + max(0, l[i] - 1) + max(0, r[i] - 1)
print(res)
