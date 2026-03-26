"""
https://www.acwing.com/problem/content/5398/
"""

lst = [[] for _ in range(11)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split(" "))
    lst[a].append(b)

for i in range(10):
    lst[i].sort()

partition = n//10
res = 0
for i in range(10):
    res += sum(lst[i][0:max(0,len(lst[i])-partition)])
print(res)
