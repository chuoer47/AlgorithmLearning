"""
https://www.acwing.com/problem/content/4658/
"""

n = int(input())
arr = [0] + list(map(int, input().split(" ")))
m = int(input())
op = [list(map(int, input().split(" "))) for _ in range(0, m)]
sum_arr = [0 for i in range(0, n + 10)]
d_arr = [0 for i in range(0, n + 10)]
pre = 0
now = 0
for i in range(1, n+1):
    sum_arr[i] = sum_arr[i - 1] + arr[i]
for i in range(len(op)):
    l, r = op[i]
    pre += sum_arr[r] - sum_arr[l - 1]
    d_arr[l] += 1
    d_arr[r + 1] -= 1
for i in range(1,n+1):
    d_arr[i] = d_arr[i] + d_arr[i-1]
d_arr.sort(reverse=True)
arr.sort(reverse=True)
for i in range(0, n):
    if d_arr[i] > 0:
        now += d_arr[i] * arr[i]
print(now - pre)
