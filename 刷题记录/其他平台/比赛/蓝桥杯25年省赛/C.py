h, w = map(int, input().split())
ans = [[''] * w for _ in range(h)]
nxt = "2025"
now = 0
for i in range(h):
    for j in range(w):
        ans[i][j] = nxt[now]
        now = (now + 1) % 4
for i in range(h):
    print("".join(ans[i]))
