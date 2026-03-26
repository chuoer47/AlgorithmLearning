"""
https://www.acwing.com/problem/content/description/124/

推导公式如下，假设糖果的列表a[i]
要求 \sum{|x-ci|} 的最小值，实际上就是货仓选址的
c[i] = [0,a[1]-avg,a[1]+a[2]-2*avg,...,sum(a[i])-n*avg = 0 ]
avg = sum(a[i]) / len(a)

"""


def solve(lst):
    """仓库选址的方法"""
    n = len(lst)
    lst.sort()
    ans = 0
    for i in range(n):
        ans += abs(lst[i] - lst[n >> 1])
    return ans


n = int(input())
a = [int(input()) for _ in range(n)]
avg = sum(a) / n
c = [0 for _ in range(n)]
for i in range(n-1):
    c[i] += c[i-1] + a[i] - avg
print(int(solve(c)))