"""
https://www.acwing.com/problem/content/description/109/
"""


def dis(lst):
    """离散化lst数组"""
    n = len(lst)
    tem = [(i, lst[i]) for i in range(n)]
    tem.sort(key=lambda x: x[1])
    for i in range(n):
        lst[tem[i][0]] = i + 1


# 树状数组
def lowbit(x):
    return x & -x


def add(x, v, tr, n):
    while x <= n:
        tr[x] += v
        x += lowbit(x)


def getSum(pivot, tr):
    ans = 0
    while pivot > 0:
        ans += tr[pivot]
        pivot -= lowbit(pivot)
    return ans


if __name__ == '__main__':
    while True:
        n = int(input())
        if not n:
            break
        lst = [int(input()) for _ in range(n)]
        tr = [0] * (n + 10)
        dis(lst)  # 离散化
        ans = 0
        # 求逆序对，设计很巧妙，要是没有离散化，这样子就计算不出来逆序对了
        # 相当于对于a[i],位置为i（假设i从1开始），值为a[i]
        # 逆序对的个数为 a[1]...a[i-1]中比a[i]大的个数
        # 因此我们可以维护一个数组，该数组维护前i个的信息，求和快速求解个数
        # 为了减少时间复杂度，使用树状数组
        for i in range(1, n + 1):
            add(lst[i - 1], 1, tr, n)
            ans += i - getSum(lst[i - 1], tr)
        print(ans)
