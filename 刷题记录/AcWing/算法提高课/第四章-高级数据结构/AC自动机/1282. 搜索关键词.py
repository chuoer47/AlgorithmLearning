"""
https://www.acwing.com/problem/content/1284/
"""

"""
第一种方法
直接使用python自带的库find
TLE 通过了 12/13个数据
"""
t = int(input())
for _ in range(t):
    n = int(input())
    words = [input() for _ in range(n)]
    msg = input()
    ans = 0
    for word in words:
        if msg.find(word) != -1:
            ans += 1
    print(ans)


