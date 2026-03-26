"""
https://www.acwing.com/problem/content/1294/
"""

N = 1000010
lst = [0] * N
table = []


def prime():
    """筛质数的函数"""
    for i in range(2, N):
        if lst[i] == 0:
            table.append(i)
            tem = i
            while tem < N:
                lst[tem] = 1
                tem += i


if __name__ == '__main__':
    prime()  # 打表
    dic = set(table)
    while True:
        n = int(input())
        if n == 0:
            break
        for i in table:
            if i < n and n - i in dic:
                print("{} = {} + {}".format(n, i, n - i))
                break
            elif i >= n:
                print("Goldbach's conjecture is wrong.")
