"""
https://www.acwing.com/problem/content/description/1538/
"""

n = int(input())
lst = list(map(int, input().split(" ")))
avg = sum(lst) / n
ans = 0
for i in range(n - 1):
    if lst[i] != avg:
        ans += 1
        lst[i + 1] += lst[i] - avg
print(ans)
