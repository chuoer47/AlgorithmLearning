s = input()
p = list(s.split("d"))


def helper(s):
    ans = 0
    r = e = re = -1
    n = len(s)
    for idx, v in enumerate(s):
        if v == "r":
            ans += e + 1
            r = idx
            re = max(re, e)
        elif v == "e":
            ans += r + 1
            e = idx
            re = max(re, r)
        else:
            ans += re + 1
    return ans


ans = sum(helper(x) for x in p)
print(ans)
