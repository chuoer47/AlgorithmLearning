"""
https://www.acwing.com/file_system/file/content/whole/index/content/3682/
相当于找到最左和最右下面计算面积
讲解：https://blog.csdn.net/revivedsun/article/details/52420679
"""


def solve(lst: list, c):  # lst进行了哨兵处理，很关键，lst最左和最右都为0
    stack = [0]  # 单调栈
    area = 0  # 最大面积
    for i in range(1, c + 2):
        while stack and lst[stack[-1]] > lst[i]:
            x = stack.pop()
            if lst[x]:
                area = max(area, lst[x] * (i - stack[-1] - 1))
        stack.append(i)
    return area


while True:
    lst = list(map(int, input().split(' ')))
    if len(lst) == 1 and lst[0] == 0:
        break
    print(solve([0] + lst[1:] + [0], lst[0]))
