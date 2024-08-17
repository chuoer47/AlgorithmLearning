"""
https://www.acwing.com/problem/content/1295/
这个题目奇奇怪怪！?
"""


def prime():
    """筛质数的函数"""
    for i in range(2, n + 2):
        if lst[i] == 0:
            cnt = 1
            lst[i] = 1
            tem = i*i
            while tem < n + 2:
                lst[tem] = 2
                tem += i


if __name__ == '__main__':
    n = int(input())
    lst = [0] * (n + 10)
    prime()
    ans = lst[2:n + 2]
    print(max(ans))
    print(*ans)
