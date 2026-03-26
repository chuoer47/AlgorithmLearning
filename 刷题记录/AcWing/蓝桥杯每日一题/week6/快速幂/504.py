"""
https://www.acwing.com/problem/content/506/
"""


n, m, k, x = map(int, input().split(" "))
part = pow(10, k, n*m)
# print(part)
print((x+part*m)%n)
