class Data:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return other.num + self.num > self.num + other.num


n = int(input())
arr = []
for i in range(1, n + 1):
    # print(bin(i)[2:])
    arr.append(Data(bin(i)[2:]))
arr.sort(reverse=True)
ans = ""
for i in range(len(arr)):
    ans += arr[i].num
# print(ans)
print(int("0b" + ans, 2))
