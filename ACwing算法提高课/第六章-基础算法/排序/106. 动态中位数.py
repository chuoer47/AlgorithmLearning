"""
https://www.acwing.com/problem/content/108/
"""

# from heapq import *

"""
第一种，直接暴力
TLE 通过了 2/4个数据
"""
# p = int(input())
# for _ in range(p):
#     stack = []
#     lst = []  # 录入数据
#     res = []  # 存答案的数组
#     num, m = map(int, input().strip().split(" "))
#     for _ in range(m // 10 + 1):
#         lst.extend(list(map(int, input().strip().split(" "))))
#     lst.reverse()
#     while lst:
#         stack.append(lst.pop())
#         stack.sort()
#         if len(stack) % 2:
#             res.append(stack[len(stack) // 2])
#     print(num, len(res))
#     i = 0
#     while i < len(res):
#         print(*res[i:i + 10])
#         i += 10


"""
第二种，采用最大堆和最小堆的方式实现
"""
from heapq import *

p = int(input())
for _ in range(p):
    maxStack = []
    minStack = []
    lst = []  # 录入数据
    res = []  # 存答案的数组
    num, m = map(int, input().strip().split(" "))
    for _ in range(m // 10 + 1):
        lst.extend(list(map(int, input().strip().split(" "))))
    lst.reverse()
    lstLen = 0
    while lst:
        lstLen += 1
        now = lst.pop()
        # 要维护两个平衡的堆，下面是具体的操作
        if not minStack or now > minStack[0]:
            heappush(minStack, now)
        else:
            heappush(maxStack,-now)

        if lstLen % 2 == 0:
            # 这时候两边要一样多
            while len(minStack) > len(maxStack):
                heappush(maxStack, -heappop(minStack))
            while len(minStack) < len(maxStack):
                heappush(minStack, -heappop(maxStack))
        elif lstLen % 2:
            # 保证上面最小堆比下面最大堆多一个
            while len(minStack) - 1 > len(maxStack):
                heappush(maxStack, -heappop(minStack))
            while len(minStack) - 1 < len(maxStack):
                heappush(minStack, -heappop(maxStack))
            res.append(minStack[0])
    print(num, len(res))
    i = 0
    while i < len(res):
        print(*res[i:i + 10])
        i += 10
