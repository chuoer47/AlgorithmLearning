"""
https://www.acwing.com/problem/content/2871/
"""


def trans(c):
    return ord(c) - ord('a')


s = input()
n = len(s)
l = [0] * n
r = [0] * n
# 从左到右进行遍历
cnt = [-1] * 26  # 存取a~z最近的下标
for i in range(0, n):
    pivot = trans(s[i])
    if cnt[pivot] == -1:
        l[i] = i
        cnt[pivot] = i
    else:
        l[i] = i - cnt[pivot] - 1
        cnt[pivot] = i
# 从右到左进行遍历
cnt = [-1] * 26
for i in range(n - 1, -1, -1):
    pivot = trans(s[i])
    if cnt[pivot] == -1:
        r[i] = n - i - 1
        cnt[pivot] = i
    else:
        r[i] = cnt[pivot] - i - 1
        cnt[pivot] = i
# 加和
res = 0
for i in range(0, n):
    res += 1 + l[i] * r[i] + max(0, l[i]) + max(0, r[i])
print(res)
