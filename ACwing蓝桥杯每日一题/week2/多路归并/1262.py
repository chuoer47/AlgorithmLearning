"""
https://www.acwing.com/problem/content/description/1264/
"""


def work(end, t):
    """
    该方法为计算从0~end个鱼塘在时间t中能掉到的最大的鱼的数量。
    :param end:
    :param t:
    :return:
    """
    if t <= 0:
        return 0
    max_num = 0
    fish_num = num[0:end + 1]

    while t > 0:
        j = 0
        now_value = fish_num[0]
        # 找到最大的鱼数目的下标
        for pivot, value in enumerate(fish_num):
            # print(i, value)
            if value > now_value:
                j = pivot
                now_value = fish_num[j]
        if fish_num[j] == 0:
            break
        max_num += fish_num[j]
        fish_num[j] = max(0, fish_num[j] - d_num[j])
        t -= 1
    return max_num


n = int(input())
num = list(map(int, input().split()))
d_num = list(map(int, input().split()))
time = [0] + list(map(int, input().split()))
t = int(input())
# 构造前缀和
for i in range(1, len(time)):
    time[i] = time[i - 1] + time[i]

res = 0
for i in range(len(time)):
    if t - time[i] > 0:
        res = max(res, work(i, t - time[i]))
        # print(res)
        # print(i)
print(res)
