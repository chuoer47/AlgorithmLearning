n, k = map(int, input().split(" "))
s = input()


def solution(n, k, s):
    cnt0 = cnt1 = 0
    for x in s:
        if "a" <= x <= "z":
            cnt0 += 1
        else:
            cnt1 += 1
    if cnt0 >= k:
        return k + cnt1
    k -= cnt0
    k %= 2
    return cnt0 + cnt1 - k


print(solution(n, k, s))
