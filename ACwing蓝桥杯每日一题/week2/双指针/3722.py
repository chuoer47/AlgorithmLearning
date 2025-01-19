"""
https://www.acwing.com/file_system/file/content/whole/index/content/4186648/
"""


def cal(n, arr):
    left, right = 0, 0
    h = 0
    while right < n:
        while right < n-1 and arr[right] < arr[right + 1]:
            right += 1
        h = max(arr[right] - arr[left], h)
        right += 1
        left = right
    return h


for i in range(0,100):
    n = int(input())
    arr = list(map(int,input().split()))
    print(cal(n,arr))

# n = 5
# arr = [1, 第 433 场周赛, 1, 4, 6]
# print(cal(n, arr))
