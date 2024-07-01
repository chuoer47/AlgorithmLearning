"""
https://www.acwing.com/problem/content/1351/
逆着思路做，很简单！
想不出来就有点难度了
简单的排序
"""

m, s, c = map(int, input().strip().split(" "))
lst = [int(input()) for i in range(c)]
lst.sort()
dlst = [lst[i] - lst[i - 1] - 1 for i in range(1, c)]
dlst.sort(reverse=True)
print(lst[-1] - lst[0] - sum(dlst[0:m-1:1]) + 1)
