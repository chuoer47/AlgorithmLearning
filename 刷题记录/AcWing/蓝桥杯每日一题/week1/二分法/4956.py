n = int(input())
arr = [list(map(int, input().split())) for i in range(0, n)]
minl, minr = 0, 1e20
for i in range(0, n):
    a, b = arr[i]
    l, r = (a // (b + 1)) + 1, a // b
    minl = max(minl, l)
    minr = min(minr, r)
print(minl,minr)