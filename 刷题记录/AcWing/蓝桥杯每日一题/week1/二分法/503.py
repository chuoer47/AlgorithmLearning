"""
https://www.acwing.com/problem/content/505/
"""

n,m = map(int,input().split())
classroom = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(0,m)]
for i in range(0,m):
    num,l,r = arr[i]
    for j in range(l-1,r):
        classroom[j] = classroom[j] - num
        if classroom[j]<0:
            print(-1)
            print(i+1)
            exit(-1)
print(0)

