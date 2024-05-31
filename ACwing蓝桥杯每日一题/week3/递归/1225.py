"""
https://www.acwing.com/problem/content/description/1227/
"""

s = input().strip()  # 测试数据有问题，后面会带空格
pivot = 0


def dfs():
    global pivot
    res = 0
    while pivot < len(s):
        c = s[pivot]
        if c == '(':
            pivot += 1  # 跳过'('
            res += dfs()
            pivot += 1  # 跳过')'
        elif c == ')':
            break
        elif c == '|':
            pivot += 1  # 跳过|
            res = max(res, dfs())
        else:
            pivot += 1
            res += 1
    return res


print(dfs())
