from collections import deque


def helper(A, B):
    s1 = s2 = 0
    A = deque(A)
    B = deque(B)
    while A and B:
        a = A.popleft()
        b = B.popleft()
        if a == b:
            continue
        elif a > b:
            A.append(a)
            s1 += 1
        else:
            B.append(b)
            s2 += 1
    if s1 == s2:
        return "draw"
    elif s1 > s2:
        return "alice"
    return "bob"


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(helper(A, B))
