"""
https://www.acwing.com/problem/content/4202/
"""

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def findAll(m):
    divide.append(1)
    i = 2
    while i * i <= m:
        if m % i == 0:
            divide.append(i)
            divide.append(m // i)
        i += 1
    divide.append(m)


a, b = map(int, input().split(" "))
q = int(input())
lst = [list(map(int, input().split(" "))) for _ in range(q)]
m = gcd(a, b)
res = []
divide = []
findAll(m)
divide.sort(reverse=True)
""" 第一种写法，较为暴力"""
"""
for l, r in lst:
    if l > m:
        res.append(-1)
    else:
        flag = False
        for i in range(min(m, r), l - 1, -1):  # 取最小的循环，节约时间
            if a % i == 0 and b % i == 0:
                res.append(i)
                flag = True
                break
        if not flag:
            res.append(-1)
"""
"""第二种写法"""
for l, r in lst:
    if l > m:
        res.append(-1)
    else:
        flag = False
        for i in divide:
            if r >= i >= l:
                res.append(i)
                flag = True
                break
        if not flag:
            res.append(-1)

for i in res:
    print(i)
