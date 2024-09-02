ans = []
s = []
n = 3
left = 0
right = 0


def dfs():
    global n, left, right
    if left>n or right>n:
        return
    if left == n and right == n:
        ans.append("".join(s))
        return
    if left < n:
        s.append("(")
        left += 1
        dfs()
        s.pop()
        left -= 1
    if 0 < left <= n and left>right:
        s.append(")")
        right += 1
        dfs()
        s.pop()
        right -= 1


dfs()
print(ans)
