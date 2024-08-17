"""
https://www.acwing.com/problem/content/1292/

脑筋急转弯题目
"""
mod = 100003
if __name__ == '__main__':
    m, n = map(int, input().strip().split(" "))
    print((pow(m, n, mod) - m * pow(m - 1, n - 1, mod)) % mod)
