"""
https://www.acwing.com/problem/content/1232/
"""
from collections import Counter

n, k = map(int, input().split(" "))
arr = [0]+[int(input()) for _ in range(0, n)]
# 构造前缀和，利用同余定理
for i in range(1, n+1):
    arr[i] = (arr[i] + arr[i - 1]) % k
arr_set = Counter(arr)
res = 0
for case in arr_set.values():
    res = res + case * (case - 1) // 2
print(res)
