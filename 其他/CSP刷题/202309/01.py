n, m = map(int, input().split(" "))
arrx = []
arry = []
resx = []
resy = []
for i in range(0, n):
    x, y = map(int, input().split(" "))
    arrx.append(x)
    arry.append(y)
for i in range(0, m):
    x, y = map(int, input().split(" "))
    resx.append(x)
    resy.append(y)
sumx = sum(arrx)
sumy = sum(arry)
for i in range(0, m):
    resx[i] = resx[i] + sumx
    resy[i] = resy[i] + sumy
for i in range(0, m):
    print("%d %d" % (resx[i], resy[i]))
