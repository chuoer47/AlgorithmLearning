"""
https://www.acwing.com/problem/content/description/4649/
"""

p = 998244353
n = int(input())
g = 0
for _ in range(n):
    x, y = map(int, input().strip().split(" "))
    g = ((g + 1) * y * (pow(y - x, p - 2, p))) % p
print(g)
