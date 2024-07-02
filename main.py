rl = lambda: list(map(int, input().split()))
n = int(input())
a = rl()
b = rl()
c = rl()

# a > b + c
def win(a, b, c):
  w = sorted(
    (x - y - z for x, y, z in zip(a, b, c)),
    reverse=True
  )

  cnt, diff = -1, 0
  for i in range(n):
    if diff + w[i] <= 0:
      break

    cnt = i + 1
    diff += w[i]

  return cnt

print(max(win(a, b, c), win(b, a, c), win(c, a, b)))
