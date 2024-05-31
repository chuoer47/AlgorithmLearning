"""
单调栈
"""


def solve():  # lst进行了哨兵处理
    stack = [0]  # 单调栈
    for i in range(1, n + 1):
        while stack and lst[stack[-1]] > lst[i]:
            x = stack.pop()
        res.append(lst[stack[-1]])
        stack.append(i)
    return


n = int(input())
lst = [-1] + list(map(int, input().split(" ")))
res = []
solve()
print(*res)
