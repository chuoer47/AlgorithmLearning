n = int(input())
do = 0
undo = 0
for _ in range(n):
    a, b = map(int, input().split())
    do += (b >= a)
    undo += (b < a)
print(do, undo)
