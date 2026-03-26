from collections import deque
from math import gcd, lcm, inf


def helper(a, b):
    if a == b:
        return 1
    a, b = max(a, b), min(a, b)
    ans = inf
    for i in range(1000):
        if a > i * b:
            best = a - i * b
        else:
            best = b - i * (i * b + a)
        ans = min(ans, lcm(a + best, best + b) // gcd(a + best, best + b))

    return ans


# helper(10, 12)  # 2
# helper(4, 9) # 1
# helper(7, 7)  # 1
# helper(6, 20)  # 8
# helper(1, 1)  # 1
# 有规律，快速找一下。

# st = []
# i = 31
# best + j
# 34 - 31 = 3
# 2*j - best = 1
# j - 1 = j - 2*j - best

# # best + j + j = i
# for j in range(1, i):
#     st.append([i, j, helper(i, j)])
# for row in st:
#     print(*row)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(helper(a, b))
