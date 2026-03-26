"""
https://www.acwing.com/problem/content/description/106/
"""

n = int(input())
lst = list(map(int, input().strip().split(" ")))
lst.sort()
ans = 0
for i in range(n):
    ans += abs(lst[i] - lst[n >> 1])
print(ans)

