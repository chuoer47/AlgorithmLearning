dic = {
    "H": 1,
    "S": 2,
    "D": 3,
    "C": 4
}


def trans(s):
    return dic[s]


w = [0] + list(map(trans, input().strip()))  # 前缀和
k = int(input())
for i in range(1, len(w)):
    w[i] += w[i - 1]

ans = -1
for i in range(k, -1, -1):
    now = w[i]
    now += w[-1] - w[-1 - (k - i)]
    ans = max(ans, now)
ans = max(ans, now)
print(ans)
