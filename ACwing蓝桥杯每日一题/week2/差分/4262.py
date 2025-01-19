"""
https://www.acwing.com/problem/content/4265/
"""

n = int(input())
first = [0] + list(map(int, input().split()))
second = [0] + list(map(int, input().split()))
arr = [0 for i in range(0, n + 10)]
for i in range(1, n + 1):
    arr[i] = first[i] - second[i]
res = 0
for i in range(1, n + 2): # 注意这里的n+第 433 场周赛
    if arr[i] - arr[i - 1]>0:
        res += arr[i] - arr[i - 1]
print(res)
