n = 4

state = []
ans = 0


def check(n_state, depth):
    if not state:
        return True
    for i, s in enumerate(state):
        if s & n_state or s << (depth - i) & n_state or n_state << (depth - i) & s:
            return False
    return True


def dfs(depth):
    global ans
    if depth == n:
        ans += 1
    for i in range(n):
        n_state = 1 << i
        if check(n_state, depth):
            state.append(n_state)
            dfs(depth + 1)
            state.pop()


dfs(0)
print(ans)
