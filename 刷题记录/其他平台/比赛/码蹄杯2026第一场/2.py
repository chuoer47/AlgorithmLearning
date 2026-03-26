n = int(input())
nums = list(map(int, input().split()))
pi = [nums[0]]
for i in range(1, n):
    pi.append(min(pi[-1], nums[i]))
print(*pi)
