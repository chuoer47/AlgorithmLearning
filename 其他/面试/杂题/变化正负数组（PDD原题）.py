"""
整形数组，包含正数和负数，然后要求把数组内的所有负数移至正数的左边，且保证相对位置不变，要求时间复杂度为O(n), 空间复杂度为O(1)。
"""

import random


def move(arr: list[int]) -> list[int]:
    arr = arr[:]
    n = len(arr)
    positive_order = 1
    multiplier = 10 ** 6

    # 第一步: 给正数加上顺序信息
    for i in range(n):
        if arr[i] > 0:
            arr[i] = arr[i] * multiplier + positive_order
            positive_order += 1

    # 第二步: 双指针法将负数移到左边
    left, right = 0, 0
    while right < n:
        if arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        right += 1

    # 第三步: 对右边的正数使用抽屉原理排序
    start_positive = left
    for i in range(start_positive, n):
        while True:
            order = int(arr[i] % multiplier)
            correct_index = start_positive + order - 1
            if i == correct_index:
                break
            arr[i], arr[correct_index] = arr[correct_index], arr[i]

    # 第四步: 还原正数
    for i in range(start_positive, n):
        arr[i] = int(arr[i] // multiplier)

    return arr


def right_move(nums: list[int]) -> list[int]:
    nums = nums[:]
    nums.sort(key=lambda x: 1 if x > 0 else 0)
    return nums


def generate_random_array(length):
    array = []
    for _ in range(length):
        # 随机生成正数或负数
        num = random.choice([1, -1]) * random.randint(1, 100)
        array.append(int(num))
    return array


if __name__ == '__main__':
    for _ in range(20):
        length = 10
        nums = generate_random_array(length)
        if move(nums) != right_move(nums):
            print(nums, move(nums), right_move(nums))
