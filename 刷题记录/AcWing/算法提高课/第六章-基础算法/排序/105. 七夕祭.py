"""
https://www.acwing.com/problem/content/107/

把问题转化为糖果传递，糖果传递再转化为货舱选址问题
把行列问题合并，求两个最小值相加的结果即为答案.
"""


def solve(lst):
    """仓库选址的方法"""
    n = len(lst)
    lst.sort()
    ans = 0
    for i in range(n):
        ans += abs(lst[i] - lst[n >> 1])
    return ans


def sweetPass(a: list):
    """糖果传递问题"""
    n = len(a)
    avg = sum(a) / n
    c = [0 for _ in range(n)]
    for i in range(n - 1):
        c[i] += c[i - 1] + a[i] - avg
    return solve(c)

# 数据录入
n, m, t = map(int, input().split(" "))
row = [0] * n
col = [0] * m
for _ in range(t):
    x, y = map(int, input().split(" "))
    row[x - 1] += 1
    col[y - 1] += 1

#  行列判断
isRow, isCol = False, False
if not t % n:
    isRow = True
    rowAns = sweetPass(row)
if not t % m:
    isCol = True
    colAns = sweetPass(col)

# 输出结果
if isRow and isCol:
    print("both {}".format(int(rowAns + colAns)))
elif isRow:
    print("row {}".format(int(rowAns)))
elif isCol:
    print("column {}".format(int(colAns)))
else:
    print("impossible")
