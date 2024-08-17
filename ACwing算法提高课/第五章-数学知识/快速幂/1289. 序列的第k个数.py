"""
https://www.acwing.com/problem/content/description/1291/
语法题...
"""
mod = 200907
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, k = map(int, input().strip().split(" "))
        d1, d2 = b - a, c - b,
        q1, q2 = b / a, c / b
        if d1 == d2:  # 等差数列
            print((a + d1 * (k - 1)) % mod)
        else:
            print((a * pow(int(q1), k - 1, mod)) % mod)
